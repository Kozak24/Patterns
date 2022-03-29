from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.state.logic import OpenState

if TYPE_CHECKING:
    from behavioral.state.logic import State


class Ticket:
    def __init__(self, ticket_name: str, reporter: str, assignee: str) -> None:
        self._name = ticket_name
        self._reporter = reporter
        self._assignee = assignee
        self._state = OpenState(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def reporter(self) -> str:
        return self._reporter

    @property
    def assignee(self) -> str:
        return self._assignee

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, state: State) -> None:
        self._state = state

    def open(self) -> None:
        self._state.open()

    def in_progress(self) -> None:
        self._state.in_progress()

    def resolve(self) -> None:
        self._state.resolve()

    def close(self) -> None:
        self._state.close()
