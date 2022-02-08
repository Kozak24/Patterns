from __future__ import annotations
from typing import TYPE_CHECKING

from structural.flyweight.logic.color_factory import ColorFactory

if TYPE_CHECKING:
    from structural.flyweight.logic.color import Color


class Shape:
    color_factory = ColorFactory()

    def __init__(self, color_name: str, red: int, green: int, blue: int) -> None:
        self._color = self.color_factory.get_color(color_name, red, green, blue)
        self.shape_type = "Shape"

    @property
    def color(self) -> Color:
        return self._color

    def draw(self) -> None:
        print(f"Drawn {self}")

    def __str__(self) -> str:
        return f"{self.shape_type} with {self.color}"
