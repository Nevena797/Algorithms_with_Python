"""Algorithms and Data Structures 1 AI - Linked Lists."""

from dataclasses import dataclass
import sys
from typing import Any, Iterator, Sequence, overload, override


@dataclass
class MyListNode:
    value: int
    prev_node: "MyListNode | None" = None
    next_node: "MyListNode | None" = None


class MySortedDoublyLinkedList(Sequence[int]):
    """A base class providing a doubly linked list representation."""

    @overload
    def __init__(self) -> None:
        """Initializes a new SortedDoublyLinkedList."""
        ...

    @overload
    def __init__(self, head: MyListNode, tail: MyListNode, size: int):
        """Initializes a new SortedDoublyLinkedList using predefined `head` and `tail`.

        Used for testing.
        """
        ...

    def __init__(
            self,
            head: "MyListNode | None" = None,
            tail: "MyListNode | None" = None,
            size: int = 0,
    ) -> None:
        self._head = head
        self._tail = tail
        self._size = size

    @override
    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    @override
    def __iter__(self) -> Iterator[int]:
        node = self._head
        while node:
            yield node.value
            node = node.next_node

    @override
    def __reversed__(self) -> Iterator[int]:
        node = self._tail
        while node:
            yield node.value
            node = node.prev_node

    @overload
    def __getitem__(self, index: int) -> int:
        ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[int]:
        ...

    @override
    def __getitem__(self, index: int | slice) -> int | Sequence[int]:
        # proper implementation of Sequence interface
        if isinstance(index, slice):
            rv = []
            for idx in range(*index.indices(len(self))):
                rv.append(self[idx])
            return rv
        if isinstance(index, int) and index < 0:
            raise IndexError("Index out of range")
        return self._get_value(index)

    def _get_value(self, index: int) -> int:
        """Return the value (elem) at position "index" without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            int: Retrieved value.

        Raises:
            IndexError: If the passed index out of range.
        """

        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        if index < self._size // 2:
            node = self._head
            for _ in range(index):
                node = node.next_node
        else:
            node = self._tail
            for _ in range(self._size - index - 1):
                node = node.prev_node

        return node.value

    @override
    def index(self, value: Any, start: int = 0, stop: int = sys.maxsize) -> int:
        """Return the index of the first occurrence of `value` in the list.

        Args:
            val (Any): Value to be searched.
            start (int): A number representing where to start the search.
            stop (int): A number representing where to end the search.

        Raises:
            ValueError: If the given value isn't found.
            
        Returns:
            int: Retrieved index.
        """
        if not isinstance(value, int):
            raise ValueError(f"{value} is not in list.")
        if start < 0:
            start = 0
        if stop > self._size:
            stop = self._size

        node = self._head
        idx = 0

        while node is not None:
            if idx >= start and idx < stop:
                if node.value == value:
                    return idx
            node = node.next_node
            idx += 1
        raise ValueError(f"{value} is not in list.")

    def insert(self, val: int) -> None:
        """Add a new node containing "val" to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            TypeError: If val is not an int.
        """
        if not isinstance(val, int):
            raise TypeError("Value must be int")

        new_node = MyListNode(val)

        # insert at beginning
        if self._head is None:
            self._head = self._tail = new_node
            self._size += 1
            return

        if val < self._head.value:
            new_node.next_node = self._head
            self._head.prev_node = new_node
            self._head = new_node
            self._size += 1
            return
        # insert in the end
        if val >= self._tail.value:
            new_node.prev_node = self._tail
            self._tail.next_node = new_node
            self._tail = new_node
            self._size += 1
            return
        node = self._head

        # insert in the middle
        while node is not None:
            if val < node.value:
                prev = node.prev_node

                new_node.next_node = node
                new_node.prev_node = prev

                prev.next_node = new_node
                node.prev_node = new_node

                self._size += 1
                return
            node = node.next_node

    def remove(self, val: int) -> None:
        """Remove the first occurrence of the parameter "val".

        Args:
            val (int): Value to be removed.

        Raises:
            ValueError: If `val` is not present.
        """
        if not isinstance(val, int):
            raise ValueError(f"{val} is not in list.")

        node = self._head

        while node is not None:
            if node.value == val:
                # 1.removing head
                if node.prev_node is None:
                    self._head = node.next_node
                    if self._head:
                        self._head.prev_node = None
                    else:
                        self._tail = None
                # 2. removing tail
                elif node.next_node is None:
                    self._tail = node.prev_node
                    self._tail.next_node = None
                # 3. removing from middle
                else:
                    prev = node.prev_node
                    nxt = node.next_node

                    prev.next_node = nxt
                    nxt.prev_node = prev

                self._size -= 1
                return
            node = node.next_node
        raise ValueError(f"{val} is not in list.")

    def remove_all(self, val: int) -> int:
        """Remove all occurrences of the parameter "val".

        Args:
            val (int): Value to be removed.

        Returns:
            int: the number of elements removed.
        """
        if not isinstance(val, int):
            return 0
        node = self._head
        count = 0

        while node is not None:
            next_node = node.next_node

            if node.value == val:
                if node.prev_node is None:
                    self._head = node.next_node

                    if self._head:
                        self._head.prev_node = None
                    else:
                        self._tail = None

                elif node.next_node is None:
                    self._tail = node.prev_node
                    self._tail.next_node = None

                else:
                    prev = node.prev_node
                    nxt = node.next_node
                    prev.next_node = nxt
                    nxt.prev_node = prev

                self._size -= 1
                count += 1
            node = next_node
        return count

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        node = self._head

        while node is not None and node.next_node is not None:
            if node.value == node.next_node.value:
                duplicate = node.next_node
                node.next_node = duplicate.next_node

                if duplicate.next_node is not None:
                    duplicate.next_node.prev_node = node
                else:
                    self._tail = node

                self._size -= 1
            else:
                node = node.next_node

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the "n" highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            TypeError: If the passed value n is not an int.
            ValueError: If the passed value n is out of range.
        """
        if not isinstance(n, int):
            raise TypeError("n must be int")
        if n <= 0 or n > self._size:
            raise ValueError("n is out of range")

        remove_count = self._size - n

        for _ in range(remove_count):
            if self._head is not None:
                self._head = self._head.next_node
                if self._head is not None:
                    self._head.prev_node = None
                else:
                    self._tail = None
                self._size -= 1

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        node = self._head

        while node is not None:
            next_node = node.next_node

            if node.value % 2 == 0:
                if node.prev_node is None:
                    self._head = node.next_node
                    if self._head:
                        self._head.prev_node = None
                    else:
                        self._tail = None

                elif node.next_node is None:
                    self._tail = node.prev_node
                    self._tail.next_node = None

                else:
                    prev = node.prev_node
                    nxt = node.next_node
                    prev.next_node = nxt
                    nxt.prev_node = prev

                self._size -= 1
            node = next_node

    def filter_even(self) -> None:
        """Filter the list to only contain even values."""
        node = self._head

        while node is not None:
            next_node = node.next_node

            if node.value % 2 != 0:

                if node.prev_node is None:
                    self._head = node.next_node
                    if self._head:
                        self._head.prev_node = None
                    else:
                        self._tail = None

                elif node.next_node is None:
                    self._tail = node.prev_node
                    self._tail.next_node = None

                else:
                    prev = node.prev_node
                    nxt = node.next_node
                    prev.next_node = nxt
                    nxt.prev_node = prev

                self._size -= 1
            node = next_node
