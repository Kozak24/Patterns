from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int

    def __str__(self) -> str:
        return f"{self.name} {self.price} G."
