# Error handlers

from fsi.ui import fail, br


def unknown_command(cmd):
    br()
    fail(f"Unknown command: {cmd}\nRun 'fsi --help' for available commands")


def handle_interrupt():
    from fsi.ui import info
    br()
    info("Interrupted.")
    br()


def handle_exception(e):
    fail(str(e))