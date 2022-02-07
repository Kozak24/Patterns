from structural.flyweight.logic.color_factory import ColorFactory


def main() -> None:
    color_factory = ColorFactory()
    red = color_factory.get_color("Red", 1, 2, 3)
    blue = color_factory.get_color("Red", 1, 2, 3)

    print(red is blue)


if __name__ == "__main__":
    main()
