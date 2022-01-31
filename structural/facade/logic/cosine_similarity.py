from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CosineSimilarity:
    def __init__(self) -> None:
        self._vectorizer = TfidfVectorizer()

    def compare(self, text1: str, text2: str) -> float:
        tfidf = self._vectorizer.fit_transform([text1, text2])
        similarity = cosine_similarity(tfidf, tfidf)[0][1]

        return similarity * 100
