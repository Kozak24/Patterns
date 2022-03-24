from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.visitor.data import Human, Car


class BaseVisitor(ABC):
    @abstractmethod
    def visit_human(self, npc: Human) -> None:
        pass

    @abstractmethod
    def visit_car(self, npc: Car) -> None:
        pass
