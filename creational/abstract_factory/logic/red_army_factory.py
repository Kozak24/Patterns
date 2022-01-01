from creational.abstract_factory.logic.army_factory import ArmyFactory
from creational.abstract_factory.data.soldiers import RedSoldier
from creational.abstract_factory.data.tanks import RedTank


class RedArmyFactory(ArmyFactory):
    def get_soldier(self):
        return RedSoldier(100, 52)

    def get_tank(self):
        return RedTank(1100, 500)
