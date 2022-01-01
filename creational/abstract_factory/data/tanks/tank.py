from abc import ABC, abstractmethod


class Tank(ABC):
    _ID = 0
    _TANK_TYPE = "Tank"

    def __init__(self, hp, attack):
        self._id = Tank._ID
        self._hp = hp
        self._attack = attack
        Tank._ID += 1

    @abstractmethod
    def patrol(self):
        pass

    @abstractmethod
    def shoot(self):
        pass

    def __str__(self) -> str:
        return f"{self._TANK_TYPE} with ID '{self._id}'"
