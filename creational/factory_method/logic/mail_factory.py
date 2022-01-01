from abc import ABC, abstractmethod

from creational.factory_method.data import Transport


class MailFactory(ABC):
    @abstractmethod
    def get_transport(self, transport_type) -> Transport:
        pass
