from behavioral.command.logic import Menu
from behavioral.command.logic.generators import TraderGenerator


def main() -> None:
    trader_generator = TraderGenerator()

    player = trader_generator.generate_trader("Player", 2)
    merchant = trader_generator.generate_trader("Merchant", 2)

    menu = Menu(player, merchant)
    menu.show_trade_panel()


if __name__ == "__main__":
    main()
