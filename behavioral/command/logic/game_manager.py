from behavioral.command.logic import Menu, TradeCommand
from behavioral.command.logic.generators import TraderGenerator


class GameManager:
    __GENERATE_ITEMS = 2

    def __init__(self):
        trader_generator = TraderGenerator()
        self._player = trader_generator.generate_trader("Player", self.__GENERATE_ITEMS)
        self._merchant = trader_generator.generate_trader("Merchant", self.__GENERATE_ITEMS)
        self._menu = Menu(self._player, self._merchant)

    def start(self):
        self._menu.print_welcome_info()
        self._menu.show_trade_panel()
