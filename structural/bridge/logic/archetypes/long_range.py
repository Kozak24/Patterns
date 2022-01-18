from structural.bridge.logic.archetypes.archetype import Archetype


class LongRange(Archetype):
    _ARCHETYPE = "Long Range"

    def attack(self) -> None:
        print(f"Attack from {self._ARCHETYPE} with {self.weapon} weapon")
