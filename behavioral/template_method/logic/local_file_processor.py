from behavioral.template_method.logic import FileProcessor


class LocalFileProcessor(FileProcessor):
    def _read_file(self) -> None:
        with open(self._file_path, "r", encoding="utf-8") as file_stream:
            self._file_content = file_stream.read()
