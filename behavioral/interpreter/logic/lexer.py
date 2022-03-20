import re
from typing import List, Tuple

from behavioral.interpreter.logic.tokens import Token, TokenType


class Lexer:
    def __init__(self, expression: str) -> None:
        self._expression = re.sub(" ", "", expression)

    def get_expression_tokens(self) -> List[Token]:
        symbol_index = 0
        tokens = list()

        print(self._expression)
        while symbol_index < len(self._expression):
            symbol = self._expression[symbol_index]

            if symbol == '+':
                tokens.append(Token(TokenType.PLUS, symbol))
            elif symbol == '-':
                tokens.append(Token(TokenType.MINUS, symbol))
            else:
                number_text, symbol_index = self._parse_number(symbol_index)
                tokens.append(Token(TokenType.INT, number_text))

            symbol_index += 1

        return tokens

    def _parse_number(self, index_to_start: int) -> Tuple[str, int]:
        symbol_index = index_to_start

        number_symbols = ""
        while symbol_index < len(self._expression):
            symbol = self._expression[symbol_index]

            if symbol.isdigit():
                number_symbols = f"{number_symbols}{symbol}"
            elif symbol.isalpha():
                raise ValueError("Numerical character is followed by alphabet character")
            else:
                symbol_index -= 1
                break

            symbol_index += 1

        return number_symbols, symbol_index
