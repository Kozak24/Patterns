import re


class TextFilterer:
    _TIMESTAMP_RE = r"[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}"

    def __init__(self, text: str) -> None:
        self._text = text

    def filter_text(self) -> str:
        self._text = re.sub(self._TIMESTAMP_RE, "", self._text)
        return self._text
