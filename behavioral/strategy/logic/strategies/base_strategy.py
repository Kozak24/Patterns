from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.strategy.data import Person


class BaseStrategy(ABC):
    @abstractmethod
    def represent(self, person: Person) -> str:
        pass
