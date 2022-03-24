from behavioral.visitor.data import Human, Car
from behavioral.visitor.logic import TxtConverterVisitor


def main() -> None:
    human = Human("Worker", "Jerar Fernandes", 23)
    car = Car("Sedan", "Revon Kista", 185.6, 4)

    txt_converter = TxtConverterVisitor()
    human.accept(txt_converter)
    car.accept(txt_converter)


if __name__ == "__main__":
    main()
