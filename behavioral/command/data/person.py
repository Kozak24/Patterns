from dataclasses import dataclass
from typing import List

from behavioral.command.data.item import Item


@dataclass
class Person:
    name: str
    items: List[Item]
    money: int

    def __str__(self) -> str:
        return f"{self.name}: {self.money} G."
