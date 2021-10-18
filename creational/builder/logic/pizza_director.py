from creational.builder.logic import PizzaBuilder


class PizzaDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PizzaBuilder):
        self._builder = builder

    def prepare_pizza(self):
        self._builder.make_dough() \
            .add_sauce() \
            .add_cheeses()

    def prepare_pizza_wo_cheese(self):
        self._builder.make_dough() \
            .add_sauce()
