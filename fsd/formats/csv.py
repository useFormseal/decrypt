import csv
import json
from pathlib import Path
from .formatter import Formatter


def _normalize(value):
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    result = str(value)
    if result and result[0] in ("=", "+", "-", "@", "\t"):
        result = "'" + result
    return result


class CsvFormatter(Formatter):
    name = "CSV"
    extension = "csv"

    def write(self, data: list[dict], path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not data:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write("")
            return

        fieldnames = sorted({k for d in data for k in d})
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow({k: _normalize(v) for k, v in row.items()})
