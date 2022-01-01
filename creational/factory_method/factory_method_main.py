from creational.shared.factory_data import Parcel
from creational.factory_method.logic import GroundMailFactory, GroundTransport, AirMailFactory, AirTransport


def main():
    parcel = Parcel("RO432423JK", 2.5)

    # Ground Mail Factory
    ground_mail_factory = GroundMailFactory()
    truck = ground_mail_factory.get_transport(GroundTransport.TRUCK)
    truck.parcel = parcel
    truck.load()
    truck.ship()

    train = ground_mail_factory.get_transport(GroundTransport.TRAIN)
    train.parcel = parcel
    train.load()
    train.ship()

    # Air Mail Factory
    air_mail_factory = AirMailFactory()
    airplane = air_mail_factory.get_transport(AirTransport.AIRPLANE)
    airplane.parcel = parcel
    airplane.load()
    airplane.ship()

    helicopter = air_mail_factory.get_transport(AirTransport.HELICOPTER)
    helicopter.parcel = parcel
    helicopter.load()
    helicopter.ship()


if __name__ == "__main__":
    main()
