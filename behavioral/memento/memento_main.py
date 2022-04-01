import time

from behavioral.memento.logic import Player, Caretaker


def main() -> None:
    player = Player(1, 1, 1, 1)
    caretaker = Caretaker(player)

    for level in range(1, 101):
        print(f"Finished level {level}")
        if level % 5 == 0:
            player.level_up()
            print(player)
            caretaker.backup()
            time.sleep(0)
            print()

    caretaker.print_saves()
    print(f"\nBefore restoring saved game: {player}")
    caretaker.restore_save(0)
    print(f"After restoring saved game: {player}")


if __name__ == "__main__":
    main()
