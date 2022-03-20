from behavioral.interpreter.logic.expressions.base_expression import BaseExpression


class SubtractExpression(BaseExpression):
    def __init__(self, left: BaseExpression, right: BaseExpression) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()
