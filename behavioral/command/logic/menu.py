class MenuCommand:
    ACCEPT = "A"
    CANCEL = "C"
    SELL = r"S(\d{1,})"
    BUY = r"B(\d{1,})"
    UNDO = "U"


class Menu:
    __GAME_DESCRIPTION = (
        "This example emulates trading system in games. There are two traders: Player and Merchant.\n"
        "Each trader has some amount of Gold which is displayed alongside with his name, also\n"
        "trader has items. Each item has index, name and its price. To provide some randomness\n"
        "trader's gold, items and their price all of those are generated randomly. So each trade is\n"
        "kinda unique and sometimes due to randomness you or merchant won't be able to buy some or\n"
        "even any item if they don't have sufficient amount of Gold.\n"
    )

    def __init__(self, player, merchant):
        self._player = player
        self._merchant = merchant

    def print_game_description(self):
        print(self.__GAME_DESCRIPTION)

    @staticmethod
    def ask_for_input():
        print("Please write command to execute: ")

    def show_trade_panel(self):
        print(f"|{str(self._player):^50}|{str(self._merchant):^50}|")
        print(f"|{'':^50}|{'':^50}|")

        player_has_more_items = self._player.items_amount >= self._merchant.items_amount
        longest_inventory = self._player.items_amount if player_has_more_items else self._merchant.items_amount
        for index in range(0, longest_inventory):
            player_item = f"S{index}. {self._player.items[index]}" if len(self._player.items) > index else ""
            merchant_item = f"B{index}. {self._merchant.items[index]}" if len(self._merchant.items) > index else ""
            print(f"|{player_item:^50}|{merchant_item:^50}|")

        print()

    @staticmethod
    def get_user_input() -> str:
        user_input = input()

        return user_input
