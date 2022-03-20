from __future__ import annotations
from typing import Optional, Callable

from behavioral.iterator.logic import DfsIterator


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None,
                 iterator: Callable = DfsIterator) -> None:
        self.value = value
        self.parent = None
        self.left = left
        self.right = right
        self._iterator = iterator(self)

        self._set_parent_relationship(left)
        self._set_parent_relationship(right)

    def _set_parent_relationship(self, node) -> None:
        if node is not None:
            node.parent = self

    def __iter__(self) -> Node:
        return self._iterator

    def __repr__(self) -> str:
        return f"Node: '{self.value}'"
