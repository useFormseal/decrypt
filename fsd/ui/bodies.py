# ui/bodies.py

from fsd.ui.styles import D, G, O, R, S, W, Y, ERROR


def br():
    print()


def fail(msg):
    br()
    print(f" {ERROR}Error:{R} {msg}")
    raise SystemExit(1)


def ok(msg):
    print(f"  {G}✨{R} {msg}")


def info(msg):
    print(f"  {O}{msg}{R}")


def neutral(msg):
    br()
    print(f" \U0001f610 {msg}")
    raise SystemExit(1)


def warn(msg):
    print(f"  {Y}⚠️ {R}{msg}")