# commands/config/config.py
# Config management

import json
import sys
from pathlib import Path

from fsd.ui import br, ok, info, warn, W, D, Y, R, header
from fsd.security import keys


CONFIG_DIR = Path.home() / ".config" / "formseal-decrypt"
CONFIG_FILE = CONFIG_DIR / "config.json"


def load_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {}


def save_config(cfg):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))


def run_status():
    cfg = load_config()

    br()
    header()
    br()

    print(f"  {W}Configuration Status:{R}")
    br()

    source = cfg.get("source")
    if not source:
        warn("Not configured. Run: fsd connect")
        br()
        return

    def row(label, value, color=W):
        print(f"  {D}{label:<26}{R}{color}{value}{R}")

    row("Source:", source)

    destination = cfg.get("destination")
    row("Destination:", destination or "(not set)")

    private_key = keys.load_private_key()
    if private_key:
        row("Key Location:", keys.private_key_location())
    else:
        row("Key Location:", "Not set")

    br()

    source_path = Path(source)
    jsonl_path = Path(destination) / "formseal.decrypted.jsonl"

    print(f"  {W}Decryption Status:{R}")
    br()

    source_entries = sum(1 for _ in open(source_path, encoding="utf-8") if _.strip())
    decrypted_entries = (
        sum(1 for _ in open(jsonl_path, encoding="utf-8") if _.strip())
        if jsonl_path.exists()
        else 0
    )

    row("Entries in source:", str(source_entries))
    row("Decrypted entries:", str(decrypted_entries))

    last_decrypt = cfg.get("last_decrypt")
    if last_decrypt:
        ts = last_decrypt.split(".")[0].replace("T", " ")
        row("Last decrypt:", ts)

    last_format = cfg.get("last_format")
    if last_format:
        row("Last decrypt format:", last_format)

    br()


def run_disconnect(args=None):
    args = args or []
    wipe = "--wipe" in args

    if wipe:
        br()
        print(f"{Y}THIS WILL DELETE EVERYTHING.{R}")
        print(f"Config, private key, AND decrypted messages will be deleted.")
    else:
        br()
        print(f"{Y}This will delete config and private key.{R}")
        print(f"Decrypted messages will NOT be affected.")
    br()
    sys.stdout.write(f"  Continue? [y/N]: ")
    sys.stdout.flush()
    confirm = input().strip().lower()

    if confirm != "y":
        br()
        info("Cancelled.")
        br()
        return

    cfg = load_config()

    if wipe:
        destination = cfg.get("destination")
        if destination:
            dest_dir = Path(destination)
            if dest_dir.exists():
                for f in dest_dir.glob("formseal.decrypted.*"):
                    f.unlink()

    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()

    keys.clear_all()

    br()
    if wipe:
        ok("Disconnected. Everything wiped.")
    else:
        ok("Disconnected. Config and private key cleared.")
    br()