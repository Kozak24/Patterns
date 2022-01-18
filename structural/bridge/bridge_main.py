from structural.bridge.logic.archetypes import LongRange, MidRange, CloseRange
from structural.bridge.logic.races import Human, Orc


WEAPONS_PER_RACE_DICT = {
    Human: {
        LongRange: "Cannon",
        MidRange: "Wooden Bow",
        CloseRange: "Sword",
    },
    Orc: {
        LongRange: "Mortier",
        MidRange: "Crossbow",
        CloseRange: "Machete",
    }
}


def main() -> None:
    for race_class in (Human, Orc):

        weapons_per_archetype_dict = WEAPONS_PER_RACE_DICT.get(race_class)
        for archetype_class in (LongRange, MidRange, CloseRange):
            weapon = weapons_per_archetype_dict.get(archetype_class)
            archetype = archetype_class(weapon)

            race = race_class(archetype)
            print(race)
            race.attack()
            print()


if __name__ == "__main__":
    main()
