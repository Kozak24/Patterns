from __future__ import annotations
import copy

from creational.prototype.data import Fraction


class Soldier:
    _ID_COUNT = 0
    _MANUAL_DEEP_COPY_ATTRS = ("_fraction", "_id")

    def __init__(self, hp: int, attack: int, fraction: Fraction):
        self._id = Soldier._ID_COUNT
        self.hp = hp
        self.attack = attack
        self.fraction = fraction
        Soldier._ID_COUNT += 1

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, hp: int):
        self._hp = hp

    @property
    def attack(self) -> int:
        return self._attack

    @attack.setter
    def attack(self, attack: int):
        self._attack = attack

    @property
    def fraction(self) -> int:
        return self._fraction

    @fraction.setter
    def fraction(self, fraction: int):
        self._fraction = fraction

    def clone(self) -> Soldier:
        return self.__deepcopy__(self.__dict__)

    def __deepcopy__(self, memodict={}) -> Soldier:
        instance = Soldier.__new__(Soldier)
        instance._id = Soldier._ID_COUNT + 1
        instance.fraction = self.fraction

        for attr_name, value in self.__dict__.items():
            if attr_name not in self._MANUAL_DEEP_COPY_ATTRS:
                setattr(instance, attr_name, copy.deepcopy(value, memodict))

        Soldier._ID_COUNT += 1

        return instance

    def __str__(self) -> str:
        return f"Soldier with ID '{self._id}', HP '{self.hp}' and Attack '{self.attack}' from {self.fraction}"
