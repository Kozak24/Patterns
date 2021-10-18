from enum import Enum


class SauceEnum(Enum):
    bbq = 0
    pesto = 1
    garlic = 2

    def __str__(self) -> str:
        return self.name
