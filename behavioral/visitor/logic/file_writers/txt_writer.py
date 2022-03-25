from behavioral.visitor.logic.file_writers import FileWriter


class TxtWriter(FileWriter):
    EXTENSION = ".txt"

    def save_file(self, content: str) -> None:
        with open(self._path, 'w', encoding='utf-8') as file_stream:
            file_stream.write(content)
