from dataclasses import dataclass

from behavioral.visitor.data import NPC
from behavioral.visitor.logic import BaseVisitor


@dataclass
class Human(NPC):
    type: str
    name: str
    age: int

    def accept(self, visitor: BaseVisitor) -> None:
        visitor.visit_human(self)
