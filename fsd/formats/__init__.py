# formats/__init__ — Formatter registry and lookup

from .formatter import Formatter
from .csv import CsvFormatter
from .jsonl import JsonlFormatter
from .json import JsonFormatter
from .md import MarkdownFormatter

FORMATTERS: dict[str, type[Formatter]] = {
    "csv": CsvFormatter,
    "jsonl": JsonlFormatter,
    "json": JsonFormatter,
    "md": MarkdownFormatter,
}


def get_formatter(format_name: str) -> Formatter:
    """Look up a formatter by name (case-insensitive, stripped)."""
    key = format_name.strip().lower()
    cls = FORMATTERS.get(key)
    if not cls:
        available = ", ".join(dict.fromkeys(c.name for c in FORMATTERS.values()))
        raise ValueError(f"Unknown format: {format_name}. Available: {available}")
    return cls()


def get_format_names() -> str:
    """Return comma-separated list of available format display names."""
    return ", ".join(dict.fromkeys(c.name for c in FORMATTERS.values()))
