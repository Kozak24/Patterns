from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.visitor.logic import BaseVisitor

if TYPE_CHECKING:
    from behavioral.visitor.data import Human, Car


class TxtConverterVisitor(BaseVisitor):
    def visit_human(self, npc: Human) -> str:
        human_txt = f"Type: {npc.type}\nName: {npc.name}\nAge: {npc.age}\n"

        return human_txt

    def visit_car(self, npc: Car) -> str:
        car_txt = f"Type: {npc.type}\nName: {npc.name}\n" \
                  f"Max Speed: {npc.max_speed}\nPassengers Capacity: {npc.passenger_capacity}"

        return car_txt
