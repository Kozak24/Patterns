from structural.bridge.logic.archetypes.archetype import Archetype


class MidRange(Archetype):
    _ARCHETYPE = "Mid-Range"

    def attack(self) -> None:
        print(f"Attack from {self._ARCHETYPE}")
