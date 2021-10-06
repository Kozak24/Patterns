from logic import MargaritaBuilder, PizzaDirector


def main():
    pizza_builder = MargaritaBuilder()
    pizza_director = PizzaDirector()
    pizza_director.builder = pizza_builder

    # Margarita with default ingredients
    pizza_director.prepare_pizza()
    pizza = pizza_builder.bake()
    print(pizza, end="\n\n")

    # Margarita without cheese
    pizza_builder.reset()
    pizza_director.prepare_pizza_wo_cheese()
    pizza = pizza_builder.bake()
    print(pizza, end="\n\n")


if __name__ == "__main__":
    main()
