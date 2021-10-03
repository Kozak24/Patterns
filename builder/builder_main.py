from logic import PizzaBuilder
from data import DoughEnum, SauceEnum, CheeseEnum


def main():
    pizza_builder = PizzaBuilder()
    pizza = pizza_builder.make_dough(DoughEnum.thin) \
        .add_sauce(SauceEnum.bbq) \
        .add_cheese(CheeseEnum.mozzarella) \
        .add_cheese(CheeseEnum.parmesan) \
        .bake()

    print(pizza)


if __name__ == "__main__":
    main()
