import logging
from typing import Any


from structural.decorator.logic.decorator import Decorator


class LoggerDecorator(Decorator):
    def __init__(self, wrappee: Any, log_level: int = logging.INFO) -> None:
        super().__init__(wrappee)
        logging.basicConfig(level=log_level)

    def process(self, *args, **kwargs) -> None:
        logging.debug(f"Entered method with params {args if args else ''} {kwargs if kwargs else ''}")
        logging.info("Started processing")
        self.wrappee.process(*args, **kwargs)
        logging.info("Processing is completed")
        logging.debug("Left method")

