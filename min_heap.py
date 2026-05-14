"""Algorithms and Data Structures 1 AI - Queue and Heaps."""

from typing import Collection, Iterator, override


class MinHeap(Collection[int]):
    """A priority queue implementation using a min heap."""

    def __init__(self, raw_heap: list[int] | None = None):
        """Initializes a new min heap, with an optional heap array to use as a basis.

        Args:
            raw_heap (list[int] | None): A already populated heap or None. Used for testing.
        """
        self._heap: list[int] = raw_heap or []

    @property
    def container(self) -> "list[int]":
        """Returns the underlying storage container used in the heap."""
        return self._heap

    def is_empty(self) -> bool:
        """True if the min heap is empty, False otherwise."""
        return len(self._heap) == 0

    def push(self, val: int) -> None:
        """Inserts the given value into the min heap."""
        self._heap.append(val)

        index = len(self._heap) - 1

        while index > 0:
            parent = (index - 1) // 2

            if self._heap[index] < self._heap[parent]:
                self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
                index = parent
            else:
                break

    def peek(self) -> int:
        """Returns the minimum element of the heap without removing it.
        
        Raises:
            RuntimeError: if the heap is empty.
        """
        if self.is_empty():
            raise RuntimeError("Heap is empty")

        return self._heap[0]

    def pop(self) -> int:
        """Removes the minimum element of the heap and returns it.

        Raises:
            RuntimeError: if the heap is empty.
        """
        if self.is_empty():
            raise RuntimeError("Heap is empty")

        minimum = self._heap[0]
        last = self._heap.pop()

        if not self.is_empty():
            self._heap[0] = last

            index = 0

            while True:
                left = 2 * index + 1
                right = 2 * index + 2
                smallest = index

                if left < len(self._heap) and self._heap[left] < self._heap[smallest]:
                    smallest = left

                if right < len(self._heap) and self._heap[right] < self._heap[smallest]:
                    smallest = right

                if smallest != index:
                    self._heap[index],self._heap[smallest] = self._heap[smallest], self._heap[index]
                    index = smallest
                else:
                    break
        return minimum

    @override
    def __len__(self) -> int:
        """The number of elements in the min heap."""
        ...
        return len(self._heap)

    @override
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.container})"

    @override
    def __contains__(self, x: object) -> bool:
        return x in self._heap

    @override
    def __iter__(self) -> Iterator[int]:
        return iter(self._heap)
