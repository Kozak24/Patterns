from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.chain_of_responsibility.data import Human


class BaseHandler(ABC):
    def __init__(self, human: Human, handler: BaseHandler = None):
        self._human = human
        self._next_handler = handler

    @property
    def next_handler(self) -> Optional[BaseHandler]:
        return self._next_handler

    @next_handler.setter
    def next_handler(self, handler: BaseHandler) -> None:
        if not isinstance(handler, BaseHandler):
            raise Exception("Handler should be derived from BaseHandler class")

        self._next_handler = handler

    def handle(self) -> None:
        self._process_handle()
        self._call_next_handler()

    @abstractmethod
    def _process_handle(self) -> None:
        pass

    def _call_next_handler(self) -> None:
        if self._next_handler is not None:
            self._next_handler.handle()
