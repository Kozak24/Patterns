from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.observer.data import Topic
    from behavioral.observer.logic import NewsSubscriber


class NewsPublisher:
    def __init__(self) -> None:
        self._subscribers = []

    def subscribe(self, subscriber: NewsSubscriber) -> None:
        if subscriber not in self._subscribers:
            print(f"\n{subscriber} subscribed to newsletters")
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: NewsSubscriber) -> None:
        if subscriber in self._subscribers:
            print(f"\n{subscriber} unsubscribed from newsletters")
            self._subscribers.remove(subscriber)

    def publish_article(self, name: str, topics: List[Topic]) -> None:
        print(f"\nPublishing new Article: '{name}' with Topics: '{', '.join(map(lambda topic: topic.value, topics))}'")
        for subscriber in self._subscribers:
            subscriber.receive_newsletter(name, topics)
