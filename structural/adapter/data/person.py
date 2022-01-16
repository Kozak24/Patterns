from dataclasses import dataclass


@dataclass
class Person:
    name: str
    last_name: str
    age: int

    def __str__(self):
        return f"{self.name} {self.last_name} {self.age} years"
