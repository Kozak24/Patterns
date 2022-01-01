from creational.factory_method.data import Transport


class Helicopter(Transport):
    def load(self) -> None:
        print(f"Parcel '{self.parcel}' is loaded into {Helicopter.__name__} {self}")

    def ship(self) -> None:
        print(f"Parcel '{self.parcel}' is shipped by {Helicopter.__name__} {self}")
