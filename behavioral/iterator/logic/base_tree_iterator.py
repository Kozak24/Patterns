from __future__ import annotations
from typing import TYPE_CHECKING, List, Generator
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from behavioral.iterator.data import Node


class BaseTreeIterator(ABC):
    def __init__(self, node: Node, visited: List[Node] = None) -> None:
        self._visited = visited if visited is not None else list()
        self._node = node
        self._items = list(self._search_nodes())
        self._index = 0
        self._max_index = len(self._items)

    def _is_visited(self, node: Node) -> bool:
        is_visited = False

        if node in self._visited:
            is_visited = True
        else:
            self._visited.append(node)

        return is_visited

    @abstractmethod
    def _search_nodes(self) -> Generator:
        pass
