from structural.composite.logic.order_calculator import OrderCalculator


class Packet(list, OrderCalculator):
    def __init__(self, packet_type: str):
        super().__init__()
        self._type = packet_type

    @property
    def type(self) -> str:
        return self._type

    @property
    def is_composite(self) -> bool:
        return True
