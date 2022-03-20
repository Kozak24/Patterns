from behavioral.interpreter.logic import Lexer


def main() -> None:
    lexer = Lexer("1 + 2 - 3")
    tokens = lexer.get_expression_tokens()
    print(tokens)


if __name__ == "__main__":
    main()
