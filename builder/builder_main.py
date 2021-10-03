from logic import ClassicPizzaBuilder


def main():
    pizza_builder = ClassicPizzaBuilder()
    pizza = pizza_builder.prepare() \
        .bake()
    print(pizza)


if __name__ == "__main__":
    main()
