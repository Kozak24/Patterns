from data import Pizza, DoughEnum, SauceEnum


def main():
    pizza = Pizza()
    pizza.dough = DoughEnum.thin
    pizza.sauce = SauceEnum.garlic
    print(pizza)


if __name__ == "__main__":
    main()
