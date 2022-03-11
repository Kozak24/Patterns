class Menu:
    def __init__(self, player, merchant):
        self._player = player
        self._merchant = merchant

    def show_trade_panel(self):
        print(f"|{str(self._player):^50}|{str(self._merchant):^50}|")
        print(f"|{'':^50}|{'':^50}|")

        player_has_more_items = self._player.items_amount >= self._merchant.items_amount
        longest_inventory = self._player.items_amount if player_has_more_items else self._merchant.items_amount
        for index in range(0, longest_inventory):
            player_item = f"S{index}. {self._player.items[index]}" if len(self._player.items) > index else ""
            merchant_item = f"B{index}. {self._merchant.items[index]}" if len(self._merchant.items) > index else ""
            print(f"|{player_item:^50}|{merchant_item:^50}|")
