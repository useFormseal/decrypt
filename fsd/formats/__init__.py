# formats/__init__.py

from .formatter import Formatter
from .jsonl import JsonlFormatter
from .json import JsonFormatter
from .md import MarkdownFormatter

FORMATTERS: dict[str, type[Formatter]] = {
    "jsonl": JsonlFormatter,
    "json": JsonFormatter,
    "md": MarkdownFormatter,
}


def get_formatter(format_name: str) -> Formatter:
    formatter_class = FORMATTERS.get(format_name)
    if not formatter_class:
        available = ", ".join(FORMATTERS.keys())
        raise ValueError(f"Unknown format: {format_name}. Available: {available}")
    return formatter_class()


def get_format_names() -> str:
    return ", ".join(fmt.name for fmt in FORMATTERS.values())


def get_extension(format_name: str) -> str:
    return FORMATTERS[format_name].extension