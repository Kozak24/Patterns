from behavioral.strategy.data import Person
from behavioral.strategy.logic import PersonRepresenter
from behavioral.strategy.logic.strategies import JsonStrategy, XmlStrategy


def main() -> None:
    person = Person("Jerar", "Fernandes", 23)
    print("\nRepresenting as JSON:")
    person_representer = PersonRepresenter(person, JsonStrategy())
    person_representer.represent()

    print("\nRepresenting as XML:")
    person_representer.represent_strategy = XmlStrategy()
    person_representer.represent()




if __name__ == "__main__":
    main()
