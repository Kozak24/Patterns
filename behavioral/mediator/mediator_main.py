from time import sleep
from random import randrange

from behavioral.mediator.data import Person, City
from behavioral.mediator.logic import AlarmMediator, AirAlarmService


def main() -> None:
    alarm_mediator = AlarmMediator()
    air_alarm_service = AirAlarmService(alarm_mediator)

    andrew = Person("Andrew", City.KYIV, alarm_mediator)
    dmytro = Person("Dmytro", City.KYIV, alarm_mediator)
    marie = Person("Marie", City.DONETSK, alarm_mediator)
    markiian = Person("Markiian", City.ZHYTOMYR, alarm_mediator)

    for city in City:
        air_alarm_service.notify_air_alarm(city)
        sleep(randrange(3, 7))

    for city in reversed(City):
        air_alarm_service.notify_air_alarm_stop(city)
        sleep(randrange(3, 7))


if __name__ == "__main__":
    main()
