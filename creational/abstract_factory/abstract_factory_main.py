from creational.abstract_factory.logic import BlueArmyFactory, RedArmyFactory


def main():
    # Blue army
    blue_army_factory = BlueArmyFactory()
    blue_soldier = blue_army_factory.get_soldier()
    blue_soldier.shoot()

    blue_tank = blue_army_factory.get_tank()
    blue_tank.shoot()

    # Red army
    red_army_factory = RedArmyFactory()
    red_soldier = red_army_factory.get_soldier()
    red_soldier.shoot()

    red_tank = red_army_factory.get_tank()
    red_tank.shoot()


if __name__ == "__main__":
    main()
