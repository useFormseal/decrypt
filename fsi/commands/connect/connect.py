# Connect command

import sys
from pathlib import Path

from fsi.ui import br, fail, ok, info, warn, G, W, D, C, Y, O, R, HEAD, OK, header
from fsi.commands.config.config import load_config, save_config
from fsi.security import keys


def _parse_args(args):
    parsed = {}
    for arg in args:
        if ":" not in arg:
            continue
        key, value = arg.split(":", 1)
        parsed[key] = value
    return parsed


def run(args):
    parsed = _parse_args(args)

    cfg = load_config()
    if cfg.get("source"):
        fail(f"Already configured.\nRun 'fsi disconnect' first.")

    print()
    header("setup")
    print()

    cfg = load_config()

    source = parsed.get("source")
    if not source:
        try:
            sys.stdout.write(f"  Source File [ciphertexts.jsonl]: ")
            sys.stdout.flush()
            source = input().strip()
            if not source:
                source = "ciphertexts.jsonl"
        except KeyboardInterrupt:
            br()
            info("Cancelled.")
            br()
            return

    destination = parsed.get("destination")
    if not destination:
        try:
            sys.stdout.write(f"  Destination File [decrypted.jsonl]: ")
            sys.stdout.flush()
            destination = input().strip()
            if not destination:
                destination = "decrypted.jsonl"
        except KeyboardInterrupt:
            br()
            info("Cancelled.")
            br()
            return

    private_key = parsed.get("private-key")
    if not private_key:
        try:
            sys.stdout.write(f"  Private Key: ")
            sys.stdout.flush()
            private_key = input().strip()
        except KeyboardInterrupt:
            br()
            info("Cancelled.")
            br()
            return

    if not private_key:
        fail("Private key is required")

    source_path = Path(source).expanduser().resolve()
    destination_path = Path(destination).expanduser().resolve()

    if not source_path.exists():
        fail(f"Source file not found: {source}")

    try:
        destination_path.parent.mkdir(parents=True, exist_ok=True)
    except Exception:
        fail("Could not create destination folder. Check permissions.")

    cfg["source"] = str(source_path)
    cfg["destination"] = str(destination_path)
    save_config(cfg)

    keys.save_private_key(private_key)

    print()
    print(f"{G}{OK}{R} Saved!")
    print()
    print(f"  Run {W}fsi decrypt{R} to decrypt messages")
    print()