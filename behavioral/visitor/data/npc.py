from dataclasses import dataclass
from abc import ABC, abstractmethod

from behavioral.visitor.logic import BaseVisitor


@dataclass
class NPC(ABC):
    type: str
    name: str

    @abstractmethod
    def accept(self, visitor: BaseVisitor) -> None:
        pass
