class Human:
    def __init__(self, hp: int, attack: int, defense: int):
        self._hp = hp
        self._attack = attack
        self._defense = defense

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, hp: int) -> None:
        self._hp = hp

    @property
    def attack(self) -> int:
        return self._attack

    @attack.setter
    def attack(self, attack: int) -> None:
        self._attack = attack

    @property
    def defense(self) -> int:
        return self._defense

    @defense.setter
    def defense(self, defense: int) -> None:
        self._defense = defense

    def __str__(self) -> str:
        return f"Human with '{self.hp}' HP, '{self.attack}' Attack and '{self.defense}' Defense"
