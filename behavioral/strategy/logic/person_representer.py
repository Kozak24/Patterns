from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.strategy.logic.strategies import BaseStrategy, JsonStrategy

if TYPE_CHECKING:
    from behavioral.strategy.data import Person


class PersonRepresenter:
    def __init__(self, person: Person, strategy: BaseStrategy = JsonStrategy()) -> None:
        self._person = person
        self._represent_strategy = strategy

    def represent(self) -> None:
        print(self._represent_strategy.represent(self._person))

    @property
    def represent_strategy(self) -> BaseStrategy:
        return self._represent_strategy

    @represent_strategy.setter
    def represent_strategy(self, represent_strategy: BaseStrategy) -> None:
        self._represent_strategy = represent_strategy
