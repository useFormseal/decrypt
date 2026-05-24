from fsd.formats import FORMATTERS
from fsd.ui import br, header
from fsd.ui.styles import G, R, W, GRAY


def run():
    br()
    header("available export formats")
    br()

    print(f"  {GRAY}Export formats are derived projections of the canonical JSONL ledger.{R}")
    br()

    for key, fmt_cls in FORMATTERS.items():
        fmt = fmt_cls()
        mark = "(canonical)" if key == "jsonl" else ""
        print(f"  {W}{key:<8}{R} {G}{fmt.name:<16}{R} {mark}")
    br()
