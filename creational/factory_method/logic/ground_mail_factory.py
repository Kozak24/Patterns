from creational.factory_method.logic.mail_factory import MailFactory
from creational.factory_method.data import Transport, Truck, Train


class GroundTransport:
    TRUCK = 0
    TRAIN = 1


class GroundMailFactory(MailFactory):
    TRANSPORT_TYPES_DICT = {
        GroundTransport.TRUCK: Truck,
        GroundTransport.TRAIN: Train,
    }

    def get_transport(self, transport_type_id) -> Transport:
        try:
            return self.TRANSPORT_TYPES_DICT[transport_type_id]()
        except KeyError:
            raise ValueError(
                f"{GroundMailFactory.__name__} doesn't support creation of '{transport_type_id}' transport type"
            )
