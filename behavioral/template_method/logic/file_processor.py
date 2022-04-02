from abc import ABC, abstractmethod


class FileProcessor(ABC):
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._file_content = None

    def process(self) -> None:
        print(f"Reading file from {self._file_path}")
        self.read_file()

    @abstractmethod
    def read_file(self) -> None:
        pass

    def print_content(self) -> None:
        pass
