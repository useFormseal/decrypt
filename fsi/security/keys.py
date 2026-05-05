# Credential storage (keyring + JSON fallback)

import json
import base64
from pathlib import Path

try:
    import keyring
    HAS_KEYRING = True
except ImportError:
    HAS_KEYRING = False

SERVICE = "formseal-inbox"

CONFIG_DIR = Path.home() / ".config" / "formseal-inbox"
SECRETS_FILE = CONFIG_DIR / "secrets.json"


def _ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def _load_secrets() -> dict:
    if not SECRETS_FILE.exists():
        return {}
    try:
        return json.loads(SECRETS_FILE.read_text())
    except:
        return {}


def _save_secrets(secrets: dict):
    if not secrets:
        if SECRETS_FILE.exists():
            SECRETS_FILE.unlink()
        return
    _ensure_config_dir()
    SECRETS_FILE.write_text(json.dumps(secrets, indent=2))


def save_private_key(private_key: str) -> bool:
    """Save private key to OS keyring. Falls back to JSON if keyring fails."""
    if HAS_KEYRING:
        try:
            keyring.set_password(SERVICE, "private-key", private_key)
            return True
        except Exception:
            pass

    secrets = _load_secrets()
    secrets["private-key"] = base64.b64encode(private_key.encode()).decode()
    _save_secrets(secrets)
    return True


def load_private_key() -> str | None:
    """Load private key from OS keyring. Falls back to JSON if not in keyring."""
    if HAS_KEYRING:
        try:
            key = keyring.get_password(SERVICE, "private-key")
            if key:
                return key
        except Exception:
            pass

    secrets = _load_secrets()
    encoded = secrets.get("private-key")
    if encoded:
        return base64.b64decode(encoded.encode()).decode().strip()
    return None


def delete_private_key():
    """Delete private key from keyring."""
    if HAS_KEYRING:
        try:
            keyring.delete_password(SERVICE, "private-key")
            return
        except Exception:
            pass

    secrets = _load_secrets()
    secrets.pop("private-key", None)
    _save_secrets(secrets)


def private_key_location() -> str:
    """Check where private key is stored."""
    if HAS_KEYRING:
        try:
            if keyring.get_password(SERVICE, "private-key"):
                return "OS Keychain"
        except Exception:
            pass

    secrets = _load_secrets()
    if "private-key" in secrets:
        return "Config File"
    return "Not set"


def clear_all():
    """Clear all secrets."""
    delete_private_key()