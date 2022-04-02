from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.strategy.logic.strategies import BaseStrategy

if TYPE_CHECKING:
    from behavioral.strategy.data import Person


class JsonStrategy(BaseStrategy):
    def represent(self, person: Person) -> str:
        json_represent = f'{{\n' \
                         f'    "first_name": "{person.first_name}",\n' \
                         f'    "second_name": "{person.second_name}",\n' \
                         f'    "age": {person.age}\n' \
                         f'}}'

        return json_represent
