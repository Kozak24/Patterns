from dataclasses import dataclass
from typing import Any

from behavioral.visitor.data import NPC
from behavioral.visitor.logic import BaseVisitor


@dataclass
class Car(NPC):
    type: str
    name: str
    max_speed: float
    passenger_capacity: int

    def accept(self, visitor: BaseVisitor) -> Any:
        return visitor.visit_car(self)
