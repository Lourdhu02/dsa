"""Binary Indexed (Fenwick) tree for prefix-sum queries / point updates."""

from __future__ import annotations


class BIT:
    """1-indexed BIT.  Update / prefix_sum: Θ(log n).  Space: Θ(n)."""

    def __init__(self, n: int) -> None:
        self._n = n
        self._t = [0] * (n + 1)

    def update(self, i: int, delta: int) -> None:
        """Add ``delta`` to position ``i`` (1-indexed)."""
        if not 1 <= i <= self._n:
            raise IndexError(i)
        while i <= self._n:
            self._t[i] += delta
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        """Sum of positions [1, i] (1-indexed)."""
        if not 0 <= i <= self._n:
            raise IndexError(i)
        s = 0
        while i > 0:
            s += self._t[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        """Inclusive sum of [l, r], 1-indexed."""
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
