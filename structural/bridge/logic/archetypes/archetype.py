from abc import ABC, abstractmethod


class Archetype(ABC):
    _ARCHETYPE = None

    def __init__(self, weapon: str) -> None:
        self.weapon = weapon

    @abstractmethod
    def attack(self) -> None:
        pass

    @property
    def weapon(self) -> str:
        return self._weapon

    @weapon.setter
    def weapon(self, weapon: str) -> None:
        self._weapon = weapon

    def __str__(self) -> str:
        return f"Archetype '{self._ARCHETYPE}'"
