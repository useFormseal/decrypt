# commands/help.py
# Help command - shows all available commands

from fsd.ui import br, header
from fsd.ui.styles import C, G, R, W, GRAY


def _get_help_groups():
    return {
        "Connect": [
            ("fsd connect", "configure source, destination, and private key"),
            ("fsd disconnect", "clear configuration"),
            ("fsd disconnect --wipe", "clear everything including messages"),
        ],
        "Decrypt": [
            ("fsd decrypt", "decrypt ciphertexts"),
            ("fsd decrypt --format <fmt>", "override output format"),
        ],
        "Info": [
            ("fsd status", "show configuration and decryption status"),
            ("fsd --version", "show version"),
            ("fsd --aliases", "list shorthand flags"),
            ("fsd --formats", "list available export formats"),
        ],
        "Docs": [
            ("https://github.com/useFormseal/decrypt/tree/main/docs", None),
        ],
    }


def _show_help():
    groups = _get_help_groups()
    br()
    header("help")
    br()

    for group, cmds in groups.items():
        print(f"  {GRAY}>> {group}{R}")
        print(G + " " + "─" * 44 + R)
        for cmd, desc in cmds:
            if desc:
                print(f"  {W}{cmd:<27}{R} {G}{desc}{R}")
            else:
                print(f"  {C}{cmd}{R}")
        br()


def run():
    _show_help()


def run_aliases():
    br()
    header("shorthand aliases")
    br()

    print(f" {W}Short{R}  {G}Canonical{R}")
    print(G + " " + "─" * 44 + R)
    print(f" {W}-s{R}     {G}status{R}")
    print(f" {W}-c{R}     {G}connect{R}")
    print(f" {W}-d{R}     {G}decrypt{R}")
    br()
