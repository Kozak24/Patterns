from behavioral.command.data import Item, Person
from behavioral.command.logic import Menu


def main() -> None:
    item1 = Item("Idzuna Necklace", 30)
    item2 = Item("Zendos Coat", 143)

    item3 = Item("Mankeru Shoes", 59)
    item4 = Item("Kinkaru Pants", 94)

    player = Person("Player", [item1, item2], 25)
    merchant = Person("Merchant", [item3, item4], 250)

    menu = Menu(player, merchant)
    menu.show_trade_panel()


if __name__ == "__main__":
    main()
