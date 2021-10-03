from enum import Enum


class CheeseEnum(Enum):
    mozzarella = 0
    cheddar = 1
    parmesan = 2

    def __str__(self) -> str:
        return self.name
