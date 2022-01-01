from creational.shared.factory_data import Transport


class Truck(Transport):
    def load(self) -> None:
        print(f"Parcel '{self.parcel}' is loaded into {Truck.__name__} {self}")

    def ship(self) -> None:
        print(f"Parcel '{self.parcel}' is shipped by {Truck.__name__} {self}")
