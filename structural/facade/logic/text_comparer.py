from structural.facade.logic.cosine_similarity import CosineSimilarity
from structural.facade.logic.text_filterer import TextFilterer


class TextComparer:
    def __init__(self, text1: str, text2: str) -> None:
        self._text1 = text1
        self._text2 = text2
        self._cosine_similarity = CosineSimilarity()

    def filter_text(self) -> None:
        self._text1 = TextFilterer(self._text1).filter_text()
        self._text2 = TextFilterer(self._text2).filter_text()

    def compare_text(self) -> float:
        return self._cosine_similarity.compare(self._text1, self._text2)

    def compare_text_with_filter(self) -> float:
        self.filter_text()
        return self.compare_text()
