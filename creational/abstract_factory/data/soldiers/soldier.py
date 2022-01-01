from abc import ABC, abstractmethod


class Soldier(ABC):
    _ID = 0
    _SOLDIER_TYPE = "Soldier"

    def __init__(self, hp, attack):
        self._id = Soldier._ID
        self._hp = hp
        self._attack = attack
        Soldier._ID += 1

    @abstractmethod
    def patrol(self):
        pass

    @abstractmethod
    def shoot(self):
        pass

    def __str__(self) -> str:
        return f"{self._SOLDIER_TYPE} with ID '{self._id}'"
