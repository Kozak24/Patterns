from abc import ABC, abstractmethod
import re


class FileProcessor(ABC):
    _LINE_ENDING_RE = r"[ ]*\n"
    _REPLACING_STRING = " Pattern\n"

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._file_content = None

    def process(self) -> None:
        print(f"\nProcessing file from '{self._file_path}'")
        self._read_file()
        self._process_file()

    @abstractmethod
    def _read_file(self) -> None:
        pass

    def print_content(self) -> None:
        print(f'"""\n{self._file_content}\n"""')

    def _process_file(self) -> None:
        self._file_content = re.sub(self._LINE_ENDING_RE, self._REPLACING_STRING, self._file_content)
