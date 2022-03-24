from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.visitor.logic import BaseVisitor

if TYPE_CHECKING:
    from behavioral.visitor.data import Human, Car


class TxtConverterVisitor(BaseVisitor):
    def visit_human(self, npc: Human) -> None:
        print("Visit Human")

    def visit_car(self, npc: Car) -> None:
        print("Visit Car")

