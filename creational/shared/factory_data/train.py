from creational.shared.factory_data import Transport


class Train(Transport):
    def load(self) -> None:
        print(f"Parcel '{self.parcel}' is loaded into {Train.__name__} {self}")

    def ship(self) -> None:
        print(f"Parcel '{self.parcel}' is shipped by {Train.__name__} {self}")
