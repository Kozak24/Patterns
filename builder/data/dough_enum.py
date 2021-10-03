from enum import Enum


class DoughEnum(Enum):
    thick = 0
    thin = 1

    def __str__(self) -> str:
        return self.name
