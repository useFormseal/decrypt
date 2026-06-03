# commands/help — Help command (show commands and aliases)

from fsd.ui import br, header, rule
from fsd.ui.styles import C, G, R, W, GRAY


def _get_help_groups():
    return {
        "Connect": [
            ("fsd connect", "configure source, dest, key"),
            ("fsd disconnect", "clear configuration"),
            ("fsd disconnect --wipe", "clear everything"),
        ],
        "Decrypt": [
            ("fsd decrypt", "decrypt ciphertexts"),
            ("fsd decrypt --format <fmt>", "override output format"),
        ],
        "Info": [
            ("fsd status", "show config and status"),
            ("fsd --version", "show version"),
            ("fsd --aliases", "list shorthand flags"),
            ("fsd --formats", "list export formats"),
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
        rule()
        for cmd, desc in cmds:
            if desc:
                print(f"  {W}{cmd:<27}{R} {G}{desc}{R}")
            else:
                print(f"  {C}{cmd}{R}")
        br()


def run():
    """Show help with all commands grouped by category."""
    _show_help()


def run_aliases():
    """Show shorthand alias flags (-s, -c, -d)."""
    br()
    header("shorthand aliases")
    br()

    print(f" {W}Short{R}  {G}Canonical{R}")
    rule()
    print(f" {W}-s{R}     {G}status{R}")
    print(f" {W}-c{R}     {G}connect{R}")
    print(f" {W}-d{R}     {G}decrypt{R}")
    br()
