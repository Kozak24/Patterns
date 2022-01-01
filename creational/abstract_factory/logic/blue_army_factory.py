from creational.abstract_factory.logic.army_factory import ArmyFactory
from creational.abstract_factory.data.soldiers import BlueSoldier
from creational.abstract_factory.data.tanks import BlueTank


class BlueArmyFactory(ArmyFactory):
    def get_soldier(self):
        return BlueSoldier(110, 50)

    def get_tank(self):
        return BlueTank(1000, 520)
