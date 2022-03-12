from dataclasses import dataclass
from typing import List

from behavioral.command.data.item import Item


@dataclass
class Trader:
    name: str
    items: List[Item]
    gold: int

    @property
    def items_amount(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"{self.name}: {self.gold} G."
