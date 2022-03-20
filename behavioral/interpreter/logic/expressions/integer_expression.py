from behavioral.interpreter.logic.expressions.base_expression import BaseExpression


class IntegerExpression(BaseExpression):
    def __init__(self, text: str) -> None:
        self.value = int(text)

    def interpret(self) -> int:
        return self.value
