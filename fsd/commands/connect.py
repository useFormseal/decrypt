# Connect command

import sys
from pathlib import Path

from fsd.ui import br, fail, neutral, info, ok, warn, C, W, WHITE, R, header
from fsd.commands.config import load_config, save_config
from fsd.security import keys


KNOWN_FLAGS = {"--source", "--dest", "--destination", "--private-key"}


def _parse_args(args):
    parsed = {}
    i = 0
    while i < len(args):
        arg = args[i]
        if arg.startswith("--"):
            if arg not in KNOWN_FLAGS:
                neutral(f"{WHITE}Invalid flag. Run {C}fsd --help{R}{WHITE} for available command flags.{R}")
            i += 1
            if i >= len(args):
                neutral(f"{WHITE}Flag requires a value. Run {C}fsd --help{R}{WHITE} for available command flags.{R}")
            key = arg[2:]
            parsed[key] = args[i]
        elif ":" in arg:
            key, value = arg.split(":", 1)
            parsed[key] = value
        i += 1
    return parsed


def run(args):
    parsed = _parse_args(args)

    cfg = load_config()
    if cfg.get("source"):
        br()
        warn(f"{WHITE}Already configured. Run {C}fsd disconnect{R}{WHITE} first.{R}")
        raise SystemExit(1)

    print()
    header("connect")
    print()

    source = parsed.get("source")
    if not source:
        try:
            sys.stdout.write(f"  {'Source File (ciphertexts):':<30}")
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
            sys.stdout.write(f"  {'Destination Directory:':<30}")
            sys.stdout.flush()
            destination = input().strip()
            if not destination:
                destination = "."
        except KeyboardInterrupt:
            br()
            info("Cancelled.")
            br()
            return

    private_key = parsed.get("private-key")
    if not private_key:
        try:
            sys.stdout.write(f"  {'Private Key:':<30}")
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
    cfg["format"] = "jsonl"
    save_config(cfg)

    keys.save_private_key(private_key)

    print()
    ok("Saved!")
    print(f"  Run {W}fsd decrypt{R} to decrypt messages")
    print()
