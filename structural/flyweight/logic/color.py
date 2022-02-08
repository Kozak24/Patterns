class Color:
    def __init__(self, name: str, red: int, green: int, blue: int) -> None:
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self) -> str:
        return f"{self.name} Color #{self.red:0>2x}{self.green:0>2x}{self.blue:0>2x}"
