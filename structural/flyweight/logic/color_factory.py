from structural.flyweight.logic import Color


class ColorFactory:
    _colors = {}

    def get_color(self, name: str, red: int, green: int, blue: int):
        color = self._colors.get(name)

        if color is None:
            color = Color(name, red, green, blue)
            self._colors[name] = color

        return color
