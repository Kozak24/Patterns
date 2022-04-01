import random

from behavioral.memento.logic import PlayerMemento


class Player:
    def __init__(self, level: int = 0, attack: int = 0, hp: int = 0, defense: int = 0) -> None:
        self._level = level
        self._attack = attack
        self._hp = hp
        self._defense = defense

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def defense(self) -> int:
        return self._defense

    @property
    def level(self) -> int:
        return self._level

    def level_up(self) -> None:
        self._level += 1

        self._increase_stats_randomly()

    def _increase_stats_randomly(self) -> None:
        self._hp += random.randint(0, 2)
        self._attack += random.randint(0, 1)
        self._defense += random.randint(0, 1)

    def get_snapshot(self) -> PlayerMemento:
        memento = PlayerMemento(self._level, self._attack, self._hp, self._defense)

        return memento

    def restore_from_snapshot(self, memento: PlayerMemento) -> None:
        self._level = memento.level
        self._attack = memento.attack
        self._hp = memento.hp
        self._defense = memento.defense

    def __str__(self) -> str:
        return f"Player Level: '{self._level} HP: '{self._hp}' " \
               f"Attack: '{self._attack}' and Defense '{self._defense}'"
