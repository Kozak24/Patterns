from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

from creational.builder.data.pizza import Pizza


class PizzaBuilder(ABC):
    def __init__(self, pizza: Optional[Pizza] = None):
        self._pizza = pizza if pizza is not None else Pizza()

    def reset(self) -> None:
        self._pizza = Pizza()

    def bake(self) -> Pizza:
        return self._pizza

    @abstractmethod
    def make_dough(self) -> PizzaBuilder:
        return self

    @abstractmethod
    def add_sauce(self) -> PizzaBuilder:
        pass

    @abstractmethod
    def add_cheeses(self) -> PizzaBuilder:
        pass
