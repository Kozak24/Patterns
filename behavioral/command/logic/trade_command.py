from behavioral.command.logic import Command
from behavioral.command.data import Trader, Item


class TradeCommand(Command):
    def __init__(self, seller: Trader, buyer: Trader, item: Item) -> None:
        self._seller = seller
        self._buyer = buyer
        self._item = item
        self._status = False

    def execute(self) -> bool:
        self._process_trade_operation(self._seller, self._buyer, self._item)

        return self._status

    def undo(self) -> bool:
        if self._status:
            self._process_trade_operation(self._buyer, self._seller, self._item)

        return self._status

    def _process_trade_operation(self, seller: Trader, buyer: Trader, item: Item) -> None:
        if buyer.gold >= item.price:
            seller.items.remove(item)
            buyer.items.append(item)
            seller.gold += item.price
            buyer.gold -= item.price

            self._status = True
        else:
            self._status = False
