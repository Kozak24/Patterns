from structural.flyweight.logic.shape import Shape


def main() -> None:
    red_shape = Shape("Red", 255, 0, 0)
    green_shape = Shape("Green", 0, 255, 0)
    blue_shape = Shape("Blue", 0, 0, 255)
    shapes = (red_shape, green_shape, blue_shape)
    for shape in shapes:
        shape.draw()


if __name__ == "__main__":
    main()
