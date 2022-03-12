class MenuCommand:
    ACCEPT = "A"
    CANCEL = "C"
    SELL = "S"
    BUY = "B"
    SELL_RE = r"S(\d{1,})"
    BUY_RE = r"B(\d{1,})"
    UNDO = "U"


class Menu:
    __GAME_DESCRIPTION_STR = (
        "This example emulates trading system in games. There are two traders: Player and Merchant.\n"
        "Each trader has some amount of Gold which is displayed alongside with his name, also\n"
        "trader has items. Each item has index, name and its price. To provide some randomness\n"
        "trader's gold, items and their price all of those are generated randomly. So each trade is\n"
        "kinda unique and sometimes due to randomness you or merchant won't be able to buy some or\n"
        "even any item if they don't have sufficient amount of Gold.\n"
    )
    __MENU_COMMANDS_STR = (
        "Here are listed available commands for use:\n"
        f"{MenuCommand.SELL}<num> - Sells item to the second trader, for example 'S0' or 'S1', etc\n"
        f"{MenuCommand.BUY}<num> - Buys item from the second trader, for example 'B0' or 'B1', etc\n"
        f"{MenuCommand.ACCEPT} - Accepts trading and immediately finishes execution\n"
        f"{MenuCommand.CANCEL} - Cancels/Undos all made operations\n"
        f"{MenuCommand.UNDO} - Undos last made operation\n"
    )
    __INPUT_STR = "Please write command to execute: "

    def __init__(self, player, merchant) -> None:
        self._player = player
        self._merchant = merchant

    def print_game_description(self) -> None:
        print(self.__GAME_DESCRIPTION_STR)

    def print_menu_commands(self) -> None:
        print(self.__MENU_COMMANDS_STR)

    def show_trade_panel(self) -> None:
        print(f"|{str(self._player):^50}|{str(self._merchant):^50}|")
        print(f"|{'':^50}|{'':^50}|")

        player_has_more_items = self._player.items_amount >= self._merchant.items_amount
        longest_inventory = self._player.items_amount if player_has_more_items else self._merchant.items_amount
        for index in range(0, longest_inventory):
            player_item = f"S{index}. {self._player.items[index]}" if len(self._player.items) > index else ""
            merchant_item = f"B{index}. {self._merchant.items[index]}" if len(self._merchant.items) > index else ""
            print(f"|{player_item:^50}|{merchant_item:^50}|")

        print()

    def get_user_input(self) -> str:
        print(self.__INPUT_STR, end="")
        user_input = input()
        print()

        return user_input
