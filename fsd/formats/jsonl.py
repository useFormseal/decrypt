# formats/jsonl.py

import json
from pathlib import Path
from .formatter import Formatter


class JsonlFormatter(Formatter):
    name = "JSON Lines"
    extension = "jsonl"

    def write(self, data: list[dict], path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            for msg in data:
                f.write(json.dumps(msg, ensure_ascii=False) + "\n")