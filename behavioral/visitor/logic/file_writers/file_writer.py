from typing import Any
from abc import ABC, abstractmethod


class FileWriter:
    EXTENSION = None

    def __init__(self, path: str) -> None:
        self._path = path

    @abstractmethod
    def save_file(self, content: Any) -> None:
        pass
