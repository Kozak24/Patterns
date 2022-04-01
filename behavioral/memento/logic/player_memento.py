class PlayerMemento:
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

    def __repr__(self) -> str:
        return f"PlayerMemento(level={self._level}, hp={self._hp}, attack={self._attack}, defense={self._defense})"

    def __str__(self) -> str:
        return f"Level: '{self._level}  HP: '{self._hp}' " \
               f"Attack: '{self._attack}' and Defense '{self._defense}'"
