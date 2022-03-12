import re

from behavioral.command.data import Trader
from behavioral.command.logic import Menu, MenuCommand, TradeCommand
from behavioral.command.logic.generators import TraderGenerator


class GameManager:
    __GENERATE_ITEMS = 2

    def __init__(self) -> None:
        trader_generator = TraderGenerator()
        self._player = trader_generator.generate_trader("Player", self.__GENERATE_ITEMS)
        self._merchant = trader_generator.generate_trader("Merchant", self.__GENERATE_ITEMS)
        self._menu = Menu(self._player, self._merchant)
        self._command_stack = list()
        self._continue_trading = True

    def start(self) -> None:
        self._menu.print_game_description()
        self._run_game()

    def _run_game(self) -> None:
        while self._continue_trading:
            self._menu.show_trade_panel()
            self._menu.ask_for_input()
            user_input = self._menu.get_user_input()
            self._handle_menu_command(user_input)

    def _handle_menu_command(self, user_input: str) -> None:
        user_input = user_input.upper()

        if MenuCommand.UNDO == user_input:
            self._undo_last_action()
        elif MenuCommand.ACCEPT == user_input:
            self._accept_trade()
        elif MenuCommand.CANCEL == user_input:
            self._undo_all_actions()
        elif match := re.match(MenuCommand.BUY, user_input):
            item_index = int(match.group(1))
            self._trade_item(item_index, self._merchant, self._player)
        elif match := re.search(MenuCommand.SELL, user_input):
            item_index = int(match.group(1))
            self._trade_item(item_index, self._player, self._merchant)
        else:
            print("Invalid command\n")

    def _undo_last_action(self) -> None:
        if self._command_stack:
            last_command = self._command_stack.pop()
            last_command.undo()
        else:
            print("Can't Undo any action since there is no actions in stack\n")

    def _undo_all_actions(self) -> None:
        self._undo_last_action()

        while self._command_stack:
            self._undo_last_action()

    def _accept_trade(self) -> None:
        self._continue_trading = False
        print("Trading is finished")

    def _trade_item(self, item_index: int, seller: Trader, buyer: Trader) -> None:
        if seller.items_amount <= item_index:
            print(f"{seller.name} doesn't have item with index {item_index}\n")
        else:
            item = seller.items[item_index]
            trade_command = TradeCommand(seller, buyer, item)

            if trade_command.execute():
                self._command_stack.append(trade_command)
                print(f"{buyer.name} successfully bought {item.name}\n")
            else:
                print(f"{buyer.name} can't afford to buy {item.name} for {item.price} G.\n")
