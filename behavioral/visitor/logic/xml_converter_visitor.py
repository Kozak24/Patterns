from __future__ import annotations
from typing import TYPE_CHECKING
import xml.etree.cElementTree as ET

from behavioral.visitor.logic import BaseVisitor

if TYPE_CHECKING:
    from behavioral.visitor.data import Human, Car


class XmlConverterVisitor(BaseVisitor):
    def visit_human(self, npc: Human) -> ET.Element:
        human_xml = ET.Element("root")
        ET.SubElement(human_xml, "type").text = npc.type
        ET.SubElement(human_xml, "name").text = npc.name
        ET.SubElement(human_xml, "age").text = str(npc.age)

        return human_xml

    def visit_car(self, npc: Car) -> ET.Element:
        car_xml = ET.Element("root")
        ET.SubElement(car_xml, "type").text = npc.type
        ET.SubElement(car_xml, "name").text = npc.name
        ET.SubElement(car_xml, "max_speed").text = str(npc.max_speed)
        ET.SubElement(car_xml, "passenger_capacity").text = str(npc.passenger_capacity)

        return car_xml
