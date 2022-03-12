from behavioral.command.logic import Menu
from behavioral.command.logic.generators import TraderGenerator


def main() -> None:
    player_generator = TraderGenerator("Player", 2)
    merchant_generator = TraderGenerator("Merchant", 2)

    player = player_generator.generate_person()
    merchant = merchant_generator.generate_person()

    menu = Menu(player, merchant)
    menu.show_trade_panel()


if __name__ == "__main__":
    main()
