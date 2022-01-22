import logging

from structural.decorator.logic import PerformanceDecorator, LoggerDecorator, Stub


def main() -> None:
    stub = Stub(5)
    performance_wrapper = PerformanceDecorator(stub)
    logger_wrapper = LoggerDecorator(performance_wrapper, logging.DEBUG)
    logger_wrapper.process(2)


if __name__ == "__main__":
    main()
