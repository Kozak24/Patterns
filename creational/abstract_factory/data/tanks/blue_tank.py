from creational.abstract_factory.data.tanks.tank import Tank


class BlueTank(Tank):
    _TANK_TYPE = "Blue Tank"

    def patrol(self):
        print(f"{self} is patrolling")

    def shoot(self):
        damage = self._attack * 1.05
        print(f"{self} shot the enemy with {damage} damage")