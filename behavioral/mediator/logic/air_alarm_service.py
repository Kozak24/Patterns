from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.mediator.logic import AlarmMediator
    from behavioral.mediator.data import City


class AirAlarmService:
    _ALARM_STARTED = "Warning! Air alarm!"
    _ALARM_STOPPED = "Warning! The air alarm is stopped!"

    def __init__(self, alarm_mediator: AlarmMediator) -> None:
        self._alarm_mediator = alarm_mediator

    def notify_air_alarm(self, city: City) -> None:
        print(f"\nAir Alarm Service of {city.value}: {self._ALARM_STARTED}")
        self._alarm_mediator.notify_air_alarm(city, self._ALARM_STARTED)

    def notify_air_alarm_stop(self, city: City) -> None:
        print(f"\nAir Alarm Service of {city.value}: {self._ALARM_STOPPED}")
        self._alarm_mediator.notify_air_alarm(city, self._ALARM_STOPPED)
