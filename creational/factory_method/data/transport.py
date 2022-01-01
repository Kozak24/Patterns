from abc import ABC, abstractmethod

from creational.factory_method.data import Parcel


class Transport(ABC):
    _TRANSPORT_ID = 0

    def __init__(self):
        self._parcel = None
        self._transport_id = Transport._TRANSPORT_ID
        Transport._TRANSPORT_ID += 1

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def ship(self):
        pass

    @property
    def parcel(self):
        return self._parcel

    @parcel.setter
    def parcel(self, parcel: Parcel):
        self._parcel = parcel

    @property
    def transport_id(self):
        return self._transport_id

    def __str__(self) -> str:
        return f"{self.transport_id}"
