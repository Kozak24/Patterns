from creational.prototype.data import Fraction
from creational.prototype.logic import Soldier

import random


def main():
    blue_fraction = Fraction("Blue")
    red_fraction = Fraction("Red")

    blue_soldier_proto = Soldier(100, 20, blue_fraction)
    red_soldier_proto = Soldier(100, 20, red_fraction)

    blue_army = create_army(blue_soldier_proto, 10)
    red_army = create_army(red_soldier_proto, 9)

    for blue_soldier in blue_army:
        print(blue_soldier)

    print("\n")

    for red_soldier in red_army:
        print(red_soldier)


def create_army(soldier_proto: Soldier, soldiers_amount: int = 50):
    soldiers = []

    for soldier_number in range(0, soldiers_amount):
        soldier_clone = soldier_proto.clone()
        soldier_clone.hp = random.randint(20, 26)
        soldier_clone.attack = random.randint(95, 125)
        soldiers.append(soldier_clone)

    return soldiers


if __name__ == "__main__":
    main()
