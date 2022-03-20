from typing import List, Tuple

from behavioral.interpreter.logic.tokens import Token, TokenType
from behavioral.interpreter.logic.expressions import IntegerExpression, AddExpression, SubtractExpression


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self._tokens = tokens
        self._non_terminal_expression = None
        self._terminal_expression = None
        self._left_expression = None
        self._right_expression = None
        self._result = 0

    def parse_expression(self) -> int:
        for token in self._tokens:
            if token.type == TokenType.INT:
                self._terminal_expression = IntegerExpression(token.text)
            elif token.type == TokenType.PLUS:
                self._non_terminal_expression = AddExpression
            elif token.type == TokenType.MINUS:
                self._non_terminal_expression = SubtractExpression

            self._process_terminal_expr()
            self._process_non_terminal_expr()

        return self._result

    def _process_terminal_expr(self) -> None:
        if self._terminal_expression is not None:
            if self._left_expression is None:
                self._left_expression = self._terminal_expression
            elif self._right_expression is None:
                self._right_expression = self._terminal_expression

            self._terminal_expression = None

    def _process_non_terminal_expr(self) -> None:
        if self._non_terminal_expression is not None:
            has_all_expressions = self._left_expression is not None and self._right_expression is not None

            if has_all_expressions:
                self._non_terminal_expression = self._non_terminal_expression(self._left_expression,
                                                                              self._right_expression)
                self._result = self._non_terminal_expression.interpret()
                self._left_expression, self._right_expression = self._non_terminal_expression, None
                self._non_terminal_expression = None
