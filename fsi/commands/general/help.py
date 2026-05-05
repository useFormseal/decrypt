# commands/general/help.py
# Help command - shows all available commands

from fsi.ui import br, header, cmd_line, rule
from fsi.ui.styles import C, G, R, W, GRAY


def _get_help_groups():
    return {
        "Connect": [
            ("fsi connect", "configure source, destination, and private key"),
            ("fsi disconnect", "clear configuration"),
            ("fsi disconnect --wipe", "clear everything including messages"),
        ],
        "Decrypt": [
            ("fsi decrypt", "decrypt ciphertexts"),
        ],
        "Info": [
            ("fsi status", "show configuration"),
            ("fsi --version", "show version"),
            ("fsi --aliases", "list shorthand flags"),
        ],
        "Docs": [
            ("https://github.com/grayguava/formseal-inbox", None),
        ],
    }


def _show_help():
    groups = _get_help_groups()
    br()
    header()
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