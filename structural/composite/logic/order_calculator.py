from collections.abc import Iterable
from abc import ABC


class OrderCalculator(ABC, Iterable):
    @property
    def sum(self) -> float:
        order_sum = 0
        for item in self:
            if hasattr(item, "is_composite"):
                if item.is_composite:
                    for order_value in item:
                        order_sum += order_value.sum
                else:
                    order_sum += item.value
            else:
                order_sum += item

        return order_sum
