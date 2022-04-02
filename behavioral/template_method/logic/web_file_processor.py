import requests

from behavioral.template_method.logic import FileProcessor


class WebFileProcessor(FileProcessor):
    def _read_file(self) -> None:
        self._file_content = requests.get(self._file_path).text
