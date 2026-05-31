# ui/bodies — Body text output (fail, neutral, ok, info, warn)

from fsd.ui.styles import D, G, O, R, S, W, Y, ERROR


def br():
    """Print a blank line."""
    print()


def fail(msg):
    """Print a bright-red Error: message and exit with status 1."""
    br()
    print(f" {ERROR}Error:{R} {msg}")
    raise SystemExit(1)


def ok(msg):
    """Print a success message with ✨."""
    print(f"  {G}✨{R} {msg}")


def info(msg):
    """Print an informational message."""
    print(f"  {O}{msg}{R}")


def neutral(msg):
    """Print a 😐 message for user-facing mistakes and exit with status 1."""
    br()
    print(f" \U0001f610 {msg}")
    raise SystemExit(1)


def warn(msg):
    """Print a ⚠️ warning message (non-fatal)."""
    print(f"  {Y}⚠️ {R}{msg}")