from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

from builder.data.pizza import Pizza

if TYPE_CHECKING:
    from builder.data import DoughEnum, SauceEnum, CheeseEnum


class PizzaBuilder(ABC):
    def __init__(self, pizza: Optional[Pizza] = None):
        self._pizza = pizza if pizza is not None else Pizza()

    def reset(self) -> None:
        self._pizza = Pizza()

    @abstractmethod
    def prepare(self) -> PizzaBuilder:
        pass

    def bake(self) -> Pizza:
        return self._pizza

    def make_dough(self, dough: DoughEnum) -> PizzaBuilder:
        self._pizza.dough = dough

        return self

    def add_sauce(self, sauce: SauceEnum) -> PizzaBuilder:
        self._pizza.sauce = sauce

        return self

    def add_cheese(self, cheese: CheeseEnum) -> PizzaBuilder:
        self._pizza.add_cheese(cheese)

        return self

