# security/keys — Credential storage (OS keychain)

import keyring

from fsd.ui.bodies import fail

SERVICE = "formseal-decrypt"


def check_keyring() -> bool:
    try:
        keyring.get_keyring()
        keyring.set_password(SERVICE, "__probe__", "probe")
        keyring.delete_password(SERVICE, "__probe__")
        return True
    except Exception:
        return False


def save_private_key(private_key: str) -> bool:
    try:
        keyring.set_password(SERVICE, "private-key", private_key)
        return True
    except Exception:
        fail("Could not save private key to OS keychain.")


def load_private_key() -> str | None:
    try:
        return keyring.get_password(SERVICE, "private-key")
    except Exception:
        fail("Could not read private key from OS keychain.")


def delete_private_key():
    try:
        keyring.delete_password(SERVICE, "private-key")
    except Exception:
        pass


def private_key_location() -> str:
    try:
        if keyring.get_password(SERVICE, "private-key"):
            return "OS Keychain"
    except Exception:
        pass
    return "Not set"


def clear_all():
    delete_private_key()
