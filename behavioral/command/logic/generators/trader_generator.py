from random import randint
from typing import Optional

from behavioral.command.data import Trader
from behavioral.command.logic.generators import ItemsGenerator


class TraderGenerator:
    __MIN_GOLD = 0
    __MAX_GOLD = 250

    def __init__(self, name: str, items_amount: int, gold: Optional[int] = None):
        self._name = name
        self._items_amount = items_amount
        self._gold = gold if gold is not None else self._generate_random_gold()

    def _generate_random_gold(self) -> int:
        return randint(self.__MIN_GOLD, self.__MAX_GOLD)

    def generate_person(self):
        items_generator = ItemsGenerator()
        items = items_generator.generate_items(self._items_amount)
        person = Trader(self._name, items, self._gold)

        return person
