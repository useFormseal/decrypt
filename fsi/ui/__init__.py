# ui/__init__.py
# Re-export from styles and bodies

from fsi.ui.styles import (
    RESET, BOLD, DIM, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, GRAY,
    O, S, G, C, Y, M, W, D, R, HEAD, OK, TICK, CROSS, ERR
)

from fsi.ui.bodies import br, badge, fail, row, cmd_line, code, link, ok, info, warn
from fsi.ui.headers import header, rule