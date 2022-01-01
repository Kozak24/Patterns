from creational.abstract_factory.data.soldiers.soldier import Soldier


class RedSoldier(Soldier):
    _SOLDIER_TYPE = "Red Soldier"

    def patrol(self):
        print(f"{self} is patrolling")

    def shoot(self):
        damage = self._attack * 1.05
        print(f"{self} shot the enemy with {damage} damage")
