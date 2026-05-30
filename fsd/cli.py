# CLI entry point and command registry

import sys

from fsd.commands import about as cmd_about
from fsd.commands import formats as cmd_formats
from fsd.commands import help as cmd_help
from fsd.commands import version as cmd_version
from fsd.commands.config import run_status, run_disconnect
from fsd.commands.connect import run as run_connect
from fsd.commands.decrypt import run as run_decrypt
from fsd.helpers.aliases import resolve
from fsd.helpers.errors import unknown_command, handle_interrupt, handle_exception

COMMANDS = {
    "connect": ("Configure source, destination, and private key", lambda a: run_connect(a)),
    "decrypt": ("Decrypt ciphertexts", lambda a: run_decrypt(a)),
    "status": ("Show configuration status", lambda a: run_status()),
    "disconnect": ("Clear all credentials", lambda a: run_disconnect(a)),
}


def main():
    if len(sys.argv) < 2:
        cmd_about.run()
        return

    args = resolve(sys.argv[1:])
    cmd = args[0].lower()
    cmd_args = args[1:]

    if cmd == "--help":
        cmd_help.run()
        return

    if cmd == "--version":
        cmd_version.run()
        return

    if cmd == "--aliases":
        cmd_help.run_aliases()
        return

    if cmd == "--formats":
        cmd_formats.run()
        return

    if cmd not in COMMANDS:
        unknown_command()

    _, handler = COMMANDS[cmd]

    try:
        handler(cmd_args)
    except KeyboardInterrupt:
        handle_interrupt()
        sys.exit(130)
    except Exception as e:
        handle_exception(e)


if __name__ == "__main__":
    main()
