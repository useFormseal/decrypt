# fsd/cmd.py
# Command registry

from fsd.commands.config.config import run_status, run_disconnect
from fsd.commands.connect.connect import run as run_connect
from fsd.commands.decrypt.decrypt import run as run_decrypt


COMMANDS = {
    "connect": ("Configure source, destination, and private key", lambda a: run_connect(a)),
    "decrypt": ("Decrypt ciphertexts", lambda a: run_decrypt(a)),
    "status": ("Show configuration status", lambda a: run_status()),
    "disconnect": ("Clear all credentials", lambda a: run_disconnect(a)),
}