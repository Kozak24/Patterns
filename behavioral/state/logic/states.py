from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.state.logic import Ticket


class State(ABC):
    def __init__(self, ticket: Ticket) -> None:
        self._ticket = ticket

    def open(self) -> None:
        print("Changed ticket state to Open")
        self._ticket.state = OpenState(self._ticket)

    def in_progress(self) -> None:
        print("Changed ticket state to In Progress")
        self._ticket.state = InProgressState(self._ticket)

    def resolve(self) -> None:
        print("Changed ticket state to Resolved")
        self._ticket.state = ResolvedState(self._ticket)

    def close(self) -> None:
        print("Changed ticket state to Closed")
        self._ticket.state = ClosedState(self._ticket)


class OpenState(State):
    def open(self) -> None:
        print("Ticket is already Opened")

    def close(self) -> None:
        print("Ticket can't be closed without resolving first")


class InProgressState(State):
    def in_progress(self) -> None:
        print("Ticket is already In Progress")

    def close(self) -> None:
        print("Ticket can't be closed without resolving first")


class ResolvedState(State):
    def resolve(self) -> None:
        print("Ticket is already Resolved")

    def in_progress(self) -> None:
        print("Ticket can't be put into In Progress state when it's resolved")


class ClosedState(State):
    def close(self) -> None:
        print("Ticket is already Closed")

    def in_progress(self) -> None:
        print("Ticket can't be put into In Progress state when it's closed")

    def resolve(self) -> None:
        print("Ticket can't be put into Resolved state when it's closed")


