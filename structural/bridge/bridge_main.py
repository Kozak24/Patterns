from structural.bridge.logic.archetypes import LongRange, MidRange, CloseRange


def main() -> None:
    for archetype_class in (LongRange, MidRange, CloseRange):
        archetype = archetype_class()
        archetype.attack()


if __name__ == "__main__":
    main()
