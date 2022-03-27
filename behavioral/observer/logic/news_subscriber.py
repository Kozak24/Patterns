from typing import List

from behavioral.observer.data import Topic


class NewsSubscriber:
    def __init__(self, name: str, topics: List[Topic]) -> None:
        self._name = name
        self._topics = topics

    def receive_newsletter(self, name: str, topics: List[Topic]) -> None:
        if self._is_interested_in_topics(topics):
            print(f"{self} received Article: '{name}', because he is interested in Topics: "
                  f"'{', '.join(map(lambda topic: topic.value, self._topics))}'")

    def _is_interested_in_topics(self, topics: List[Topic]) -> bool:
        interested_in_topics_set = set(self._topics)
        received_topics_set = set(topics)

        return any(interested_in_topics_set & received_topics_set)

    def __str__(self) -> str:
        return f"{self._name}"
