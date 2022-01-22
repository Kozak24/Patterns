from typing import Any
from abc import ABC, abstractmethod


class Decorator(ABC):
    def __init__(self, wrappee: Any):
        self.wrappee = wrappee

    @abstractmethod
    def process(self):
        pass
