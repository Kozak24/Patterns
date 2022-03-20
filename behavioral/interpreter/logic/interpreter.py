from behavioral.interpreter.logic import Lexer, Parser


class Interpreter:
    def __init__(self, expression: str) -> None:
        self._expression = expression

    def interpret(self) -> int:
        tokens = Lexer(self._expression).get_expression_tokens()
        parser = Parser(tokens)

        return parser.parse_expression()
