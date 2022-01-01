class Parcel:
    def __init__(self, parcel_id: str, weight: float) -> None:
        self.parcel_id = parcel_id
        self.weight = weight

    def __str__(self) -> str:
        return self.parcel_id
