# formats/formatter — Abstract base formatter

from abc import ABC, abstractmethod
from pathlib import Path


class Formatter(ABC):
    name: str = ""
    extension: str = ""

    @abstractmethod
    def write(self, data: list[dict], path: Path):
        """Write decrypted data to the given path in the target format."""