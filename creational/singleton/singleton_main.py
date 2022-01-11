from creational.singleton.logic import God


def main():
    god = God()
    another_god = God()

    if god != another_god:
        raise Exception("God should be equal to God")

    for _ in range(0, 7):
        god.do_something()

    another_god.do_something()


if __name__ == "__main__":
    main()