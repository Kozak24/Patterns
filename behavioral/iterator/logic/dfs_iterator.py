from __future__ import annotations
from typing import TYPE_CHECKING, Generator, List

from behavioral.iterator.logic import BaseTreeIterator

if TYPE_CHECKING:
    from behavioral.iterator.data import Node


class DfsIterator(BaseTreeIterator):
    def __init__(self, node: Node, visited: List[Node] = None) -> None:
        super().__init__(node, visited)

    def __next__(self) -> Node:
        if self._index < self._max_index:
            item = self._items[self._index]
            self._index += 1

            return item

        self._index = 0
        raise StopIteration

    def __iter__(self) -> DfsIterator:
        return self

    def _search_nodes(self) -> Generator:
        if not self._is_visited(self._node):
            yield self._node

        if self._node.left is not None:
            for node in DfsIterator(self._node.left, self._visited):
                yield node

        if self._node.right is not None:
            for node in DfsIterator(self._node.right, self._visited):
                yield node
