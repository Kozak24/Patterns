from creational.abstract_factory.data.tanks.tank import Tank


class RedTank(Tank):
    _TANK_TYPE = "Red Tank"

    def patrol(self):
        print(f"{self} is patrolling")

    def shoot(self):
        damage = self._attack * 0.98
        print(f"{self} shot the enemy with {damage} damage")
