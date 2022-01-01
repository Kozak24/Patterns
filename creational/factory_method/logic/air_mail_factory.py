from creational.factory_method.logic.mail_factory import MailFactory
from creational.shared.factory_data import Transport, Airplane, Helicopter

from enum import IntEnum


class AirTransport:
    AIRPLANE = 0
    HELICOPTER = 1


class AirMailFactory(MailFactory):
    TRANSPORT_TYPES_DICT = {
        AirTransport.AIRPLANE: Airplane,
        AirTransport.HELICOPTER: Helicopter,
    }

    def get_transport(self, transport_type_id) -> Transport:
        try:
            return self.TRANSPORT_TYPES_DICT[transport_type_id]()
        except KeyError:
            raise ValueError(
                f"{AirMailFactory.__name__} doesn't support creation of '{transport_type_id}' transport type"
            )
