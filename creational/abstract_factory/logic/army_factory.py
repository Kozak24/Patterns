from abc import ABC, abstractmethod


class ArmyFactory(ABC):
    @abstractmethod
    def get_soldier(self):
        pass

    @abstractmethod
    def get_tank(self):
        pass
