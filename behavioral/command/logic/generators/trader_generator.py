from random import randint
from typing import Optional

from behavioral.command.data import Trader
from behavioral.command.logic.generators import ItemsGenerator


class TraderGenerator:
    __MIN_GOLD = 0
    __MAX_GOLD = 450

    def __init__(self) -> None:
        self._items_generator = ItemsGenerator()

    def _generate_random_gold(self) -> int:
        return randint(self.__MIN_GOLD, self.__MAX_GOLD)

    def generate_trader(self, name: str, items_amount: int, gold: Optional[int] = None) -> Trader:
        items_generator = ItemsGenerator()
        gold = gold if gold is not None else self._generate_random_gold()
        items = items_generator.generate_items(items_amount)
        trader = Trader(name, items, gold)

        return trader
