from typing import Any, Optional, Iterable

class Node:
    def __init__(self, item: Any):
        self.item = item
        self.link = None

class LinkedList:
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        self._head = None
        self._tail = None
        self._len = 0
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self) -> int:
        return self._len

    def get_head(self) -> Any | None:
        if self._head is None:
            return None
        return self._head.item

    def get_tail(self) -> Any | None:
        if self._tail is None:
            return None
        return self._tail.item

    def add_last(self, item: Any) -> None:
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.link = new_node
            self._tail = new_node
        self._len += 1

    def add_first(self, item: Any) -> None:
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.link = self._head
            self._head = new_node
        self._len += 1

    def remove_first(self) -> Any:
        if self._head is None:
            raise RuntimeError("Empty list")
        item = self._head.item
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._len -= 1
        return item

    def remove_last(self) -> Any:
        if self._head is None:
            raise RuntimeError("Empty list")
        if self._head == self._tail:
            return self.remove_first()
        
        curr = self._head
        while curr.link != self._tail:
            curr = curr.link
            
        item = self._tail.item
        curr.link = None
        self._tail = curr
        self._len -= 1
        return item