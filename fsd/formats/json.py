# formats/json — Pretty-printed JSON formatter

import json
from pathlib import Path
from .formatter import Formatter


class JsonFormatter(Formatter):
    name = "JSON"
    extension = "json"

    def write(self, data: list[dict], path: Path):
        """Write decrypted data as a pretty-printed JSON array."""
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)