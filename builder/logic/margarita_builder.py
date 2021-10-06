from builder.logic import PizzaBuilder
from builder.data import DoughEnum, SauceEnum, CheeseEnum


class MargaritaBuilder(PizzaBuilder):
    def make_dough(self) -> PizzaBuilder:
        self._pizza.dough = DoughEnum.thin

        return self

    def add_sauce(self) -> PizzaBuilder:
        self._pizza.sauce = SauceEnum.pesto

        return self

    def add_cheeses(self) -> PizzaBuilder:
        self._pizza.add_cheese(CheeseEnum.mozzarella)

        return self
