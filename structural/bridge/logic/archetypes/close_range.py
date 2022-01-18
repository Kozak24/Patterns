from structural.bridge.logic.archetypes.archetype import Archetype


class CloseRange(Archetype):
    _ARCHETYPE = "Close Range"

    def attack(self) -> None:
        print(f"Attack from {self._ARCHETYPE}")
