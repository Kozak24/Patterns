from creational.prototype.data import Fraction


class Soldier:
    _ID = 0

    def __init__(self, hp: int, attack: int, fraction: Fraction):
        self._id = Soldier._ID
        self._hp = hp
        self._attack = attack
        self._fraction = fraction
        Soldier._ID += 1

    def __str__(self) -> str:
        return f"Soldier with ID '{self._id}'"
