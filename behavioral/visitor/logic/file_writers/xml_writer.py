import xml.etree.cElementTree as ET

from behavioral.visitor.logic.file_writers import FileWriter


class XmlWriter(FileWriter):
    EXTENSION = ".xml"

    def save_file(self, content: ET.Element) -> None:
        tree = ET.ElementTree(content)
        tree.write(self._path)
