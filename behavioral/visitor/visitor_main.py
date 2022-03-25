import os
from typing import Callable

from behavioral.visitor.data import NPC, Human, Car
from behavioral.visitor.logic import TxtConverterVisitor, XmlConverterVisitor, JsonConverterVisitor
from behavioral.visitor.logic.file_writers import TxtWriter, XmlWriter, JsonWriter

OUTPUT_PATH = "output"
CONVERTER_TO_WRITER_DICT = {
    TxtConverterVisitor: TxtWriter,
    XmlConverterVisitor: XmlWriter,
    JsonConverterVisitor: JsonWriter
}


def main() -> None:
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    human = Human("Worker", "Jerar Fernandes", 23)
    car = Car("Sedan", "Revon Kista", 185.6, 4)

    for converter_callable, file_writer_callable in CONVERTER_TO_WRITER_DICT.items():
        process_npc(human, converter_callable, file_writer_callable)
        process_npc(car, converter_callable, file_writer_callable)


def process_npc(npc: NPC, converter_callable: Callable, file_writer_callable: Callable) -> None:
    converter = converter_callable()
    npc_class = npc.__class__.__name__
    npc_data = npc.accept(converter)

    npc_data_file_name = f"{npc_class}{file_writer_callable.EXTENSION}"
    npc_data_file_path = os.path.join(OUTPUT_PATH, npc_data_file_name)

    file_writer = file_writer_callable(npc_data_file_path)
    file_writer.save_file(npc_data)

    print(f"Saved {npc_data_file_path}")


if __name__ == "__main__":
    main()
