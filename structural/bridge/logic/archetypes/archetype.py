from abc import ABC, abstractmethod


class Archetype(ABC):
    _ARCHETYPE = None

    @abstractmethod
    def attack(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Archetype '{self._ARCHETYPE}'"
