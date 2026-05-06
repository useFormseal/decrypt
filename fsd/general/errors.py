# Error handlers

from fsd.ui import fail, br


def unknown_command(cmd):
    br()
    fail(f"Unknown command: {cmd}\nRun 'fsd --help' for available commands")


def handle_interrupt():
    from fsd.ui import info
    br()
    info("Interrupted.")
    br()


def handle_exception(e):
    fail(str(e))