from typing import List


class Archetype:
    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 0

    def lvl_up(self):
        self.level += 1

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, level: int) -> None:
        self._level = level

    def __str__(self) -> str:
        return f"{self.name} with '{self.level}' level"


class Character:
    _shared_dict = {}
    _initialized = False

    def __init__(self, archetype: Archetype) -> None:
        self.__dict__ = self._shared_dict
        self.archetype = archetype

        if not self._initialized:
            self._inventory = {
                "Hat": 1,
            }
            self._initialized = True

    def add_to_inventory(self, item: str) -> None:
        if item in self._inventory:
            self._inventory[item] += 1
        else:
            self._inventory[item] = 1

    def __str__(self) -> str:
        return f"{self.archetype} and '{self._inventory}' in bag"
