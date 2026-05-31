# formats/md — Markdown table formatter

from pathlib import Path
from .formatter import Formatter


class MarkdownFormatter(Formatter):
    name = "Markdown"
    extension = "md"

    def write(self, data: list[dict], path: Path):
        """Write decrypted data as a markdown table."""
        if not data:
            return

        path.parent.mkdir(parents=True, exist_ok=True)

        headers = self._get_headers(data)
        rows = [self._flatten_row(item) for item in data]

        with open(path, "w", encoding="utf-8") as f:
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("|" + "|".join([" --- " for _ in headers]) + "|\n")
            for row in rows:
                cells = [str(row.get(h, "")) for h in headers]
                f.write("| " + " | ".join(cells) + " |\n")

    def _get_headers(self, data: list[dict]) -> list[str]:
        headers = set()
        for item in data:
            headers.update(self._flatten_row(item).keys())
        headers.discard("version")

        order = ["id", "origin", "submitted_at"]
        pinned = [h for h in order if h in headers]
        rest = sorted(h for h in headers if h not in order)
        return pinned + rest

    def _flatten_row(self, item: dict) -> dict:
        row = {}
        for key, value in item.items():
            if key == "data" and isinstance(value, dict):
                for k, v in value.items():
                    row[k] = v
            elif key not in ("data", "version"):
                row[key] = value
        return row