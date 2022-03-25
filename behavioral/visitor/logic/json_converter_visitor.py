from __future__ import annotations
from typing import Dict, Union, TYPE_CHECKING

from behavioral.visitor.logic import BaseVisitor

if TYPE_CHECKING:
    from behavioral.visitor.data import Human, Car


class JsonConverterVisitor(BaseVisitor):
    def visit_human(self, npc: Human) -> Dict[str, Union[str, int]]:
        human_dict = {
            "type": npc.type,
            "name": npc.name,
            "age": npc.age,
        }

        return human_dict

    def visit_car(self, npc: Car) -> Dict[str, Union[str, int, float]]:
        car_dict = {
            "type": npc.type,
            "name": npc.name,
            "max_speed": npc.max_speed,
            "passenger_capacity": npc.passenger_capacity,
        }

        return car_dict
