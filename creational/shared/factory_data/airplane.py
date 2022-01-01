from creational.shared.factory_data import Transport


class Airplane(Transport):
    def load(self) -> None:
        print(f"Parcel '{self.parcel}' is loaded into {Airplane.__name__} {self}")

    def ship(self) -> None:
        print(f"Parcel '{self.parcel}' is shipped by {Airplane.__name__} {self}")
