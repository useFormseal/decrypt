# helpers/errors — Error handler functions

from fsd.ui import br, fail, neutral, info, C, WHITE, R


def unknown_command():
    """Print error and exit when an unrecognized command is given."""
    neutral(f"{WHITE}This command doesn't exist. Run {C}fsd --help{R}{WHITE} for available commands.{R}")


def handle_interrupt():
    """Print interruption message and exit gracefully."""
    br()
    info("Interrupted.")
    br()


def handle_exception(e):
    """Print exception message and exit with fail()."""
    fail(str(e))
