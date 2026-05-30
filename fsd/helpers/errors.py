# Error handlers

from fsd.ui import br, fail, neutral, info, C, WHITE, R


def unknown_command():
    neutral(f"{WHITE}This command doesn't exist. Run {C}fsd --help{R}{WHITE} for available commands.{R}")


def handle_interrupt():
    br()
    info("Interrupted.")
    br()


def handle_exception(e):
    fail(str(e))
