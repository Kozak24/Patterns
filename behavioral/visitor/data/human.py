from dataclasses import dataclass

from behavioral.visitor.data import NPC


@dataclass
class Human(NPC):
    type: str
    name: str
    age: int
