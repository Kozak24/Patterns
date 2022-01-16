from xml.etree import ElementTree

from structural.adapter.logic import XmlToJsonAdapter
from structural.adapter.data import Person

DATA_FILE_REL_PATH = "data/data.xml"


def main():
    tree = ElementTree.parse(DATA_FILE_REL_PATH)
    root = tree.getroot()

    xml_to_json_adapter = XmlToJsonAdapter(root)
    jsoned_xml = xml_to_json_adapter.convert_to_json()

    persons_dict = jsoned_xml.get("persons")
    for person_dict in persons_dict.get("person"):
        print(f"Created Person from XML '{Person(**person_dict)}'")


if __name__ == "__main__":
    main()
