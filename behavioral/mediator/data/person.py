from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.mediator.logic import AlarmMediator
    from behavioral.mediator.data import City


class Person:
    def __init__(self, name: str, city: City, mediator: AlarmMediator) -> None:
        self.name = name
        self.city = city
        mediator.subscribe(self)

    def receive_alarm_notification(self, message: str) -> None:
        print(f"{self} received: {message}")

    def __str__(self) -> str:
        return f"{self.name} from {self.city.value}"
