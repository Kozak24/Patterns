from structural.composite.logic.order_calculator import OrderCalculator


class Srorder(list, OrderCalculator):
    def __init__(self, order_id: str) -> None:
        super().__init__()
        self._order_id = order_id

    @property
    def order_id(self) -> str:
        return self._order_id


class Order(list, OrderCalculator):
    def __init__(self, order_id: str) -> None:
        super().__init__()
        self._order_id = order_id

    @property
    def order_id(self) -> str:
        return self._order_id

    @property
    def is_composite(self) -> bool:
        return True
