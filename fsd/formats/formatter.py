# formats/formatter.py

from abc import ABC, abstractmethod
from pathlib import Path


class Formatter(ABC):
    name: str = ""
    extension: str = ""

    @abstractmethod
    def write(self, data: list[dict], path: Path):
        pass