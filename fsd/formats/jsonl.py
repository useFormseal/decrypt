# formats/jsonl — JSONL canonical ledger formatter

import json
from pathlib import Path
from .formatter import Formatter


class JsonlFormatter(Formatter):
    name = "JSONL"
    extension = "jsonl"

    def write(self, data: list[dict], path: Path):
        """Write decrypted data as newline-delimited JSON (canonical ledger)."""
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            for msg in data:
                f.write(json.dumps(msg, ensure_ascii=False) + "\n")