# decrypt command

import json
from datetime import datetime
from pathlib import Path

import nacl.public
import nacl.encoding

from fsd.ui import br, fail, neutral, warn, C, G, W, D, Y, R, WHITE, header
from fsd.commands.config import load_config, save_config
from fsd.security import keys
from fsd.formats import get_formatter, get_format_names


KNOWN_FLAGS = {"--format", "-f"}


def _parse_args(args):
    parsed = {}
    i = 0
    while i < len(args):
        arg = args[i]
        if arg.startswith("-"):
            if arg not in KNOWN_FLAGS:
                neutral(f"{WHITE}Invalid flag. Run {C}fsd --help{R}{WHITE} for available command flags.{R}")
            i += 1
            if i >= len(args):
                neutral(f"{WHITE}Flag requires a value. Run {C}fsd --help{R}{WHITE} for available command flags.{R}")
            key = "format"
            parsed[key] = args[i]
        i += 1
    return parsed


def run(args):
    cfg = load_config()
    cli_args = _parse_args(args)

    source = cfg.get("source")
    if not source:
        fail(f"Not configured. Run {C}fsd connect{R}")

    destination = cfg.get("destination")
    if not destination:
        fail(f"Destination not set. Run {C}fsd connect{R}")

    output_format_raw = cli_args.get("format", cfg.get("format", "jsonl"))
    try:
        output_formatter = get_formatter(output_format_raw)
    except ValueError:
        neutral(f"Invalid format. Available: {get_format_names()}")
    output_format = output_formatter.extension
    jsonl_formatter = get_formatter("jsonl")
    jsonl_path = Path(destination) / "formseal.decrypted.jsonl"

    extra_formatter = None
    extra_path = None
    if output_format != "jsonl":
        extra_formatter = output_formatter
        extra_path = Path(destination) / f"formseal.decrypted.{extra_formatter.extension}"

    private_key = keys.load_private_key()
    if not private_key:
        fail(f"Private key not set. Run {C}fsd connect{R}")

    source_path = Path(source)

    if not source_path.exists():
        fail(f"Source file not found: {source}")

    br()
    header("decrypt")
    br()

    def row(label, value, color=W):
        print(f"  {D}{label:<26}{R}{color}{value}{R}")

    row("Source:", str(source_path))
    row("Canonical:", str(jsonl_path))
    if extra_path:
        row("Export:", f"{extra_formatter.name} ({extra_path.name})")
    row("Format:", jsonl_formatter.name if not extra_formatter else extra_formatter.name)

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
        jsonl_formatter.write(decrypted, jsonl_path)
        if extra_formatter:
            extra_formatter.write(decrypted, extra_path)
        cfg["last_decrypt"] = datetime.now().astimezone().isoformat()
        cfg["last_format"] = jsonl_formatter.name if not extra_formatter else extra_formatter.name
        save_config(cfg)

    br()
    row("Processed:", total, G)
    row("Decrypted:", len(decrypted), G if len(decrypted) > 0 else D)
    row("Failed:", failed, Y if failed > 0 else D)

    if total == 0:
        br()
        warn("Source file contains no records.")
    elif failed > 0:
        br()
        warn("Some messages could not be decrypted.")
        warn("The ciphertext may be corrupted or encrypted for a different key.")

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
