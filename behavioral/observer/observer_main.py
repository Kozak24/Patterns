from behavioral.observer.data import Topic
from behavioral.observer.logic import NewsSubscriber, NewsPublisher


def main() -> None:
    subscriber1 = NewsSubscriber("Ivan", [Topic.SPORT, Topic.SCIENCE, Topic.POLITICS])
    subscriber2 = NewsSubscriber("John", [Topic.ART, Topic.TECHNOLOGY, Topic.POLITICS])

    news_publisher = NewsPublisher()
    news_publisher.subscribe(subscriber1)
    news_publisher.subscribe(subscriber2)

    news_publisher.publish_article("Bambung announced new Ralaxy X23 Smartphone", [Topic.SCIENCE, Topic.TECHNOLOGY])
    news_publisher.publish_article("Z is symbol of fascism in XXI century", [Topic.POLITICS])

    news_publisher.unsubscribe(subscriber1)

    news_publisher.publish_article("Ralevich Square has been recently sold for 1 000 000 000$", [Topic.ART])

    news_publisher.publish_article("Ressy has scored 3 goals against Nanchester United", [Topic.SPORT])


if __name__ == "__main__":
    main()
