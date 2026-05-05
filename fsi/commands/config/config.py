# commands/config/config.py
# Config management

import json
import sys
from pathlib import Path

from fsi.ui import br, fail, ok, info, warn, G, W, D, C, Y, R, HEAD, header
from fsi.security import keys


CONFIG_DIR = Path.home() / ".config" / "formseal-inbox"
CONFIG_FILE = CONFIG_DIR / "config.json"


def load_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {}


def save_config(cfg):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))


def get_token():
    pass


def get_namespace():
    pass


def run_status():
    cfg = load_config()

    br()
    header()
    br()

    print(f"  {D}Configuration Status:{R}")
    br()

    source = cfg.get("source")
    if not source:
        warn("Not configured. Run: fsi connect")
        br()
        return

    def row(label, value, color=W):
        print(f"  {D}{label:<26}{R}{color}{value}{R}")

    row("Source:", source)

    destination = cfg.get("destination")
    row("Destination:", destination or "(not set)", W if destination else D)

    private_key = keys.load_private_key()
    if private_key:
        row("Private Key:", keys.private_key_location(), G)
    else:
        row("Private Key:", "Not set", D)

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
            dest_path = Path(destination)
            if dest_path.exists():
                dest_path.unlink()

    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()

    keys.clear_all()

    br()
    if wipe:
        ok("Disconnected. Everything wiped.")
    else:
        ok("Disconnected. Config and private key cleared.")
    br()