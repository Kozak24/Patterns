from dataclasses import dataclass

from behavioral.visitor.data import NPC


@dataclass
class Car(NPC):
    type: str
    name: str
    max_speed: float
    passenger_capacity: int
