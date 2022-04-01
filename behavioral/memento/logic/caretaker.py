from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.memento.logic import Player


class Caretaker:
    _MAX_SAVES_TO_KEEP = 10
    _MAX_SAVE_INDEX = _MAX_SAVES_TO_KEEP - 1

    def __init__(self, player: Player) -> None:
        self._mementos = []
        self._player = player

    def backup(self) -> None:
        print("Saving progress...")
        memento = self._player.get_snapshot()

        self._mementos.append(memento)

        if len(self._mementos) > self._MAX_SAVES_TO_KEEP:
            print(f"There are more than {self._MAX_SAVES_TO_KEEP} saves, removing the oldest one")
            self._mementos.pop(0)

    def restore_save(self, save_index: int = _MAX_SAVE_INDEX) -> None:
        if save_index > self._MAX_SAVE_INDEX or save_index >= len(self._mementos):
            print("Wrong save is specified, no actions performed")
            return

        memento = self._mementos[save_index]
        print(f"Restoring Saved game #{save_index} {memento}")
        self._player.restore_from_snapshot(memento)

    def print_saves(self) -> None:
        print("Saved games:")
        for index, memento in enumerate(self._mementos):
            print(f"Saved game #{index}: {memento}")
