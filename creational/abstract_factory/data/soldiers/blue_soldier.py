from creational.abstract_factory.data.soldiers.soldier import Soldier


class BlueSoldier(Soldier):
    _SOLDIER_TYPE = "Blue Soldier"

    def patrol(self):
        print(f"{self} is patrolling")

    def shoot(self):
        damage = self._attack * 0.98
        print(f"{self} shot the enemy with {damage} damage")
