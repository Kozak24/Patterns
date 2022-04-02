class Person:
    def __init__(self, first_name: str, second_name: str, age: int) -> None:
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = age

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def second_name(self) -> str:
        return self.__second_name

    @property
    def age(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f"{self.first_name} {self.second_name} age {self.age}"
