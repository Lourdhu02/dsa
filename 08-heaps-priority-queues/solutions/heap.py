"""Hand-rolled binary min-heap.  Mirrors CLRS § 6.

In real Python code use ``heapq``; this exists so the data structure is
visible at least once.
"""

from __future__ import annotations

from typing import Iterable


class MinHeap:
    """Binary min-heap over Python ints (any ``<``-comparable type works)."""

    def __init__(self, items: Iterable[int] | None = None) -> None:
        self._h: list[int] = list(items) if items else []
        self._heapify()

    def __len__(self) -> int:
        return len(self._h)

    def peek(self) -> int:
        """Θ(1)."""
        return self._h[0]

    def push(self, x: int) -> None:
        """Θ(log n)."""
        self._h.append(x)
        self._sift_up(len(self._h) - 1)

    def pop(self) -> int:
        """Θ(log n)."""
        last = self._h.pop()
        if not self._h:
            return last
        out = self._h[0]
        self._h[0] = last
        self._sift_down(0)
        return out

    def _heapify(self) -> None:
        """Θ(n) — see CLRS § 6.3."""
        for i in range(len(self._h) // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2
            if self._h[i] < self._h[parent]:
                self._h[i], self._h[parent] = self._h[parent], self._h[i]
                i = parent
            else:
                return

    def _sift_down(self, i: int) -> None:
        n = len(self._h)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i
            if l < n and self._h[l] < self._h[smallest]:
                smallest = l
            if r < n and self._h[r] < self._h[smallest]:
                smallest = r
            if smallest == i:
                return
            self._h[i], self._h[smallest] = self._h[smallest], self._h[i]
            i = smallest
