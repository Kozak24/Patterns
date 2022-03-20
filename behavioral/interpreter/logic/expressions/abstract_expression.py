from abc import ABC, abstractmethod


class BaseExpression(ABC):
    @abstractmethod
    def interpret(self):
        pass
