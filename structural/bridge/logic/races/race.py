from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from structural.bridge.logic.archetypes import Archetype


class Race(ABC):
    _NAME = None

    def __init__(self, archetype: Archetype) -> None:
        self._archetype = archetype

    def attack(self) -> None:
        self._archetype.attack()

    def __str__(self) -> str:
        return f"'{self._NAME}' race of {self._archetype}"
