import json
from typing import Dict, Union

from behavioral.visitor.logic.file_writers import FileWriter


class JsonWriter(FileWriter):
    EXTENSION = ".json"

    def save_file(self, content: Dict[str, Union[str, int, float]]) -> None:
        with open(self._path, 'w', encoding='utf-8') as file_stream:
            json.dump(content, file_stream, indent=4)
