from behavioral.command.logic.command import Command


class TradeCommand(Command):
    def __init__(self, buyer, seller, item) -> None:
        self._buyer = buyer
        self._seller = seller
        self._item = item

    def execute(self) -> bool:
        pass

    def undo(self) -> bool:
        pass
