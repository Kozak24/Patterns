from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.strategy.logic.strategies import BaseStrategy

if TYPE_CHECKING:
    from behavioral.strategy.data import Person


class XmlStrategy(BaseStrategy):
    def represent(self, person: Person) -> str:
        xml_represent = f'<root>\n' \
                         f'    <first_name>{person.first_name}</first_name>\n' \
                         f'    <second_name>{person.second_name}<second_name>\n' \
                         f'    <age>{person.age}<age>\n' \
                         f'</root>'

        return xml_represent
