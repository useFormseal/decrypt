# ui/headers — Header and rule rendering

from fsd.ui.styles import C, D, G, R, W, HEAD, BORDER


def header(title=""):
    """Print a formseal-decrypt header with optional subtext."""
    if title:
        print(f"{C} \u250c\u2500 {HEAD} {R}{W}formseal-decrypt{R}     {D}\\{R}     {W}{title}{R}")
    else:
        print(f"{C} \u250c\u2500 {HEAD} {R}{W}formseal-decrypt{R}")
    print(G + " " + BORDER + R)


def rule():
    """Print a horizontal rule line."""
    print(G + " " + BORDER + R)