# Connect command

import sys
from pathlib import Path

from fsd.ui import br, fail, ok, info, warn, G, W, D, C, Y, O, R, HEAD, OK, header
from fsd.commands.config.config import load_config, save_config
from fsd.security import keys
from fsd.formats import FORMATTERS, get_format_names


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
        fail(f"Already configured.\nRun 'fsd disconnect' first.")

    print()
    header("setup")
    print()

    cfg = load_config()

    source = parsed.get("source")
    if not source:
        try:
            sys.stdout.write(f"  Source File (ciphertexts): ")
            sys.stdout.flush()
            source = input().strip()
            if not source:
                fail("Source file is required")
            if not source.endswith(".jsonl"):
                source = source + ".jsonl"
        except KeyboardInterrupt:
            br()
            info("Cancelled.")
            br()
            return

    destination = parsed.get("destination")
    if not destination:
        try:
            sys.stdout.write(f"  Destination Directory: ")
            sys.stdout.flush()
            destination = input().strip()
            if not destination:
                destination = "."
        except KeyboardInterrupt:
            br()
            info("Cancelled.")
            br()
            return

    available_formats = get_format_names()
    output_format = parsed.get("format")
    if not output_format:
        try:
            sys.stdout.write(f"  Output Format [{available_formats}]: ")
            sys.stdout.flush()
            output_format = input().strip()
            if not output_format:
                output_format = "jsonl"
        except KeyboardInterrupt:
            br()
            info("Cancelled.")
            br()
            return

    if output_format.lower() not in FORMATTERS:
        fail(f"Invalid format: {output_format}. Available: {available_formats}")

    output_format = output_format.lower()

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
    dest_dir = Path(destination).expanduser().resolve()

    if not source_path.exists():
        fail(f"Source file not found: {source}")

    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
    except Exception:
        fail("Could not create destination directory. Check permissions.")

    cfg["source"] = str(source_path)
    cfg["destination"] = str(dest_dir)
    cfg["format"] = output_format
    save_config(cfg)

    keys.save_private_key(private_key)

    print()
    print(f"{G}{OK}{R} Saved!")
    print()
    print(f"  Run {W}fsd decrypt{R} to decrypt messages")
    print()