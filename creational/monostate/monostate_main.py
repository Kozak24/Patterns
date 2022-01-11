import random

from creational.monostate.logic import Archetype, Character


def main():
    knight = Archetype("Knight")
    wizard = Archetype("Wizard")
    archetypes = (knight, wizard)

    character = change_archetype(knight)

    for i in range(0, 200):
        archetype = random.choice(archetypes)
        new_adventure(archetype)
        print(character)


def change_archetype(archetype: Archetype):
    return Character(archetype)


def new_adventure(archetype: Archetype):
    character = change_archetype(archetype)
    item = random.choice(["Hat", "Armor", "Gloves", "Pants", "Boots", "Food", "Drink", "Elixir"])
    print(f"Found '{item}' item")
    character.add_to_inventory(item)

    if random.randint(0, 2) == 1:
        character.archetype.lvl_up()


if __name__ == "__main__":
    main()
