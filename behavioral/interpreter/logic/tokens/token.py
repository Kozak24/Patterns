from behavioral.interpreter.logic.tokens.token_type import TokenType


class Token:
    def __init__(self, token_type: TokenType, text: str) -> None:
        self.type = token_type
        self.text = text

    def __repr__(self) -> str:
        return f"Token '{self.type.name}' with value '{self.text}'"
