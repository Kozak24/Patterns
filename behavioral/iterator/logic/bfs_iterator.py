from __future__ import annotations
from typing import TYPE_CHECKING, Generator, List

from behavioral.iterator.logic import BaseTreeIterator

if TYPE_CHECKING:
    from behavioral.iterator.data import Node


class BfsIterator(BaseTreeIterator):
    def __init__(self, node: Node, visited: List[Node] = None, queue: List[Node] = None) -> None:
        self._queue = queue if queue is not None else list()
        super().__init__(node, visited)

    def __next__(self) -> Node:
        if self._index < self._max_index:
            item = self._items[self._index]
            self._index += 1

            return item

        self._index = 0
        raise StopIteration

    def __iter__(self) -> BfsIterator:
        return self

    def _search_nodes(self) -> Generator:
        if not self._is_visited(self._node):
            self._queue.append(self._node)

        while self._queue:
            node = self._queue.pop(0)
            yield node

            if node.left is not None and not self._is_visited(node.left):
                self._queue.append(node.left)

            if node.right is not None and not self._is_visited(node.right):
                self._queue.append(node.right)
