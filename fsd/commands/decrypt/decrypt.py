# decrypt command

import json
from pathlib import Path

import nacl.public
import nacl.encoding

from fsd.ui import br, fail, ok, info, warn, G, W, D, C, Y, R, HEAD, header
from fsd.commands.config.config import load_config
from fsd.security import keys
from fsd.formats import get_formatter, get_extension


def run(args):
    cfg = load_config()

    source = cfg.get("source")
    if not source:
        fail("Not configured. Run: fsd connect")

    destination = cfg.get("destination")
    if not destination:
        fail("Destination not set. Run: fsd connect")

    output_format = cfg.get("format", "jsonl")
    formatter = get_formatter(output_format)

    private_key = keys.load_private_key()
    if not private_key:
        fail("Private key not set. Run: fsd connect")

    source_path = Path(source)
    dest_dir = Path(destination)
    ext = get_extension(output_format)
    dest_path = dest_dir / f"formseal.decrypted.{ext}"

    if not source_path.exists():
        fail(f"Source file not found: {source}")

    br()
    header("decrypt")
    br()

    def row(label, value, color=W):
        print(f"  {D}{label:<26}{R}{color}{value}{R}")

    row("Source:", str(source_path))
    row("Destination:", str(dest_path))
    row("Format:", output_format)

    br()

    private_key_bytes = _decode_base64url(private_key)
    if not private_key_bytes or len(private_key_bytes) != 32:
        fail("Invalid private key. Must be 32-byte base64url.")

    private_key_box = nacl.public.PrivateKey(private_key_bytes)

    decrypted = []
    failed = 0
    total = 0

    with open(source_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            total += 1
            try:
                decrypted_msg = _decrypt_line(line, private_key_box)
                decrypted.append(decrypted_msg)
            except Exception:
                failed += 1

    if decrypted:
        formatter.write(decrypted, dest_path)

    br()
    row("Processed:", total, G)
    row("Decrypted:", len(decrypted), G if len(decrypted) > 0 else D)
    row("Failed:", failed, Y if failed > 0 else D)

    if failed > 0:
        br()
        warn(f"Some messages could not be decrypted.")
        warn(f"Check that the private key is correct.")

    br()


def _decode_base64url(b64url):
    b64url = b64url.replace("-", "+").replace("_", "/")
    pad = len(b64url) % 4
    if pad:
        b64url += "=" * (4 - pad)
    try:
        import base64
        return base64.b64decode(b64url)
    except Exception:
        return None


def _decrypt_line(line, private_key_box):
    if not line.startswith("formseal."):
        raise ValueError("Invalid format: missing formseal. prefix")

    ciphertext_b64url = line[9:]
    ciphertext_bytes = _decode_base64url(ciphertext_b64url)

    if not ciphertext_bytes:
        raise ValueError("Invalid ciphertext encoding")

    sealed_box = nacl.public.SealedBox(private_key_box)
    plaintext = sealed_box.decrypt(ciphertext_bytes, encoder=nacl.encoding.RawEncoder)
    return json.loads(plaintext)