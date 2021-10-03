from builder.data import DoughEnum, SauceEnum, CheeseEnum
from builder.logic.pizza_builder import PizzaBuilder


class ClassicPizzaBuilder(PizzaBuilder):
    def prepare(self) -> PizzaBuilder:
        self.make_dough(DoughEnum.thin) \
            .add_sauce(SauceEnum.bbq) \
            .add_cheese(CheeseEnum.mozzarella) \
            .add_cheese(CheeseEnum.parmesan)

        return self
