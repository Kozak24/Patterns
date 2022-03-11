from behavioral.command.data import Item, Person


def main() -> None:
    item1 = Item("Idzuna Necklace", 30)
    item2 = Item("Zendos Coat", 143)

    item3 = Item("Mankeru Shoes", 59)
    item4 = Item("Kinkaru Pants", 94)

    player = Person("Player", [item1, item2], 25)
    merchant = Person("Merchant", [item3, item4], 250)

    while True:
        print("Select item")
        print(f"|{str(player):^50}|{str(merchant):^50}|")
        print(f"|{'':^50}|{'':^50}|")

        longest_inventory = len(player.items) if len(player.items) >= len(merchant.items) else len(merchant.items)
        for index in range(0, longest_inventory):
            player_item = f"S{index}. {player.items[index]}" if len(player.items) > index else ""
            merchant_item = f"B{index}. {merchant.items[index]}" if len(merchant.items) > index else ""
            print(f"|{player_item:^50}|{merchant_item:^50}|")
        break


if __name__ == "__main__":
    main()
