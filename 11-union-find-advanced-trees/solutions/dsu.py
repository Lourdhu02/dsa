"""Disjoint Set Union with path compression and union by rank.

α(n) amortized per op (Tarjan & van Leeuwen 1984).
"""

from __future__ import annotations


class DSU:
    def __init__(self, n: int) -> None:
        self._parent = list(range(n))
        self._rank = [0] * n
        self.count = n  # number of disjoint components

    def find(self, x: int) -> int:
        # Iterative two-pass path compression: walk to root, then assign.
        root = x
        while self._parent[root] != root:
            root = self._parent[root]
        while self._parent[x] != root:
            self._parent[x], x = root, self._parent[x]
        return root

    def union(self, x: int, y: int) -> bool:
        """Returns True if a merge happened."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self._rank[rx] < self._rank[ry]:
            rx, ry = ry, rx
        self._parent[ry] = rx
        if self._rank[rx] == self._rank[ry]:
            self._rank[rx] += 1
        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
