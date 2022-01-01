from abc import ABC, abstractmethod

from creational.shared.factory_data import Transport


class MailFactory(ABC):
    @abstractmethod
    def get_transport(self, transport_type) -> Transport:
        pass
