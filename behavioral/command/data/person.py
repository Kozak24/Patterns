from dataclasses import dataclass
from typing import List

from behavioral.command.data.item import Item


@dataclass
class Person:
    name: str
    items: List[Item]
    money: int

    @property
    def items_amount(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"{self.name}: {self.money} G."
