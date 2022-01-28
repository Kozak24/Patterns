from structural.composite.logic.order_calculator import OrderCalculator


class Product(OrderCalculator):
    def __init__(self, name: str, value: float) -> None:
        self._name = name
        self._value = value

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> float:
        return self._value

    @property
    def is_composite(self) -> bool:
        return False

    def __iter__(self) -> float:
        yield self.value
