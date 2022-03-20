from behavioral.interpreter.logic import Interpreter

EXPRESSIONS = ("1 + 2 - 3", "25 - 5 + 0", "30 - 50 - 20", "1 - 1 + 7 - 3")


def main() -> None:
    for expression in EXPRESSIONS:
        interpreter = Interpreter(expression)
        result = interpreter.interpret()
        print(f"{expression} = {result}")


if __name__ == "__main__":
    main()
