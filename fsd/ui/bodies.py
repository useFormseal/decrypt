# ui/bodies.py

from fsd.ui.styles import D, O, R, S, W, Y, BOLD, RED


def br():
    print()


def _badge(label, color):
    return f"{color}{BOLD} {label} {R}"


def fail(msg):
    br()
    print(f"{_badge('❌', RED)} {msg}")
    br()
    raise SystemExit(1)


def ok(msg):
    print(f"  {G}✨{R} {msg}")


def info(msg):
    print(f"  {O}{msg}{R}")


def warn(msg):
    print(f"{Y}⚠️ {R}{msg}")