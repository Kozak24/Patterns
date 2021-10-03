from typing import Optional, List

from builder.data.dough_enum import DoughEnum
from builder.data.sauce_enum import SauceEnum
from builder.data.cheese_enum import CheeseEnum


class Pizza:
    def __init__(self) -> None:
        self._dough: Optional[DoughEnum] = None
        self._sauce: Optional[SauceEnum] = None
        self._cheeses: List[CheeseEnum] = list()

    @property
    def dough(self) -> DoughEnum:
        return self._dough

    @dough.setter
    def dough(self, dough: DoughEnum) -> None:
        self._dough = dough

    @property
    def sauce(self) -> SauceEnum:
        return self._sauce

    @sauce.setter
    def sauce(self, sauce: SauceEnum) -> None:
        self._sauce = sauce

    @property
    def cheeses(self):
        return self._cheeses

    def add_cheese(self, cheese: CheeseEnum):
        self._cheeses.append(cheese)

    def cheeses_names(self) -> List[str]:
        cheeses_str_list = list()

        for cheese in self.cheeses:
            cheeses_str_list.append(str(cheese))

        return cheeses_str_list

    def __str__(self) -> str:
        return (
            f"Pizza with {self.dough} dough and {self.sauce} sauce {chr(10)}"
            f"Pizza has following cheese(s):{chr(10)}"
            f"{chr(10).join(self.cheeses_names())}"
        )
