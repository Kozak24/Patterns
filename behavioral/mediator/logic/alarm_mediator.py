from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.mediator.data import Person, City


class AlarmMediator:
    def __init__(self) -> None:
        self._subscribers = []

    def subscribe(self, person: Person) -> None:
        if person not in self._subscribers:
            self._subscribers.append(person)

    def notify_air_alarm(self, city: City, message: str) -> None:
        for subscriber in self._subscribers:
            if subscriber.city == city:
                subscriber.receive_alarm_notification(message)
