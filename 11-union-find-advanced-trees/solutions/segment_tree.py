"""Segment tree for range sum + point update.  Build/Query/Update Θ(log n)."""

from __future__ import annotations


class SegmentTreeSum:
    def __init__(self, data: list[int]) -> None:
        self._n = len(data)
        self._tree = [0] * (4 * max(1, self._n))
        if self._n:
            self._build(1, 0, self._n - 1, data)

    def _build(self, node: int, lo: int, hi: int, data: list[int]) -> None:
        if lo == hi:
            self._tree[node] = data[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, data)
        self._build(2 * node + 1, mid + 1, hi, data)
        self._tree[node] = self._tree[2 * node] + self._tree[2 * node + 1]

    def update(self, i: int, value: int) -> None:
        if not 0 <= i < self._n:
            raise IndexError(i)
        self._update(1, 0, self._n - 1, i, value)

    def _update(self, node: int, lo: int, hi: int, i: int, value: int) -> None:
        if lo == hi:
            self._tree[node] = value
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * node, lo, mid, i, value)
        else:
            self._update(2 * node + 1, mid + 1, hi, i, value)
        self._tree[node] = self._tree[2 * node] + self._tree[2 * node + 1]

    def range_sum(self, l: int, r: int) -> int:
        """Sum of values in inclusive range ``[l, r]``."""
        if l > r or l < 0 or r >= self._n:
            raise IndexError((l, r))
        return self._query(1, 0, self._n - 1, l, r)

    def _query(self, node: int, lo: int, hi: int, l: int, r: int) -> int:
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self._tree[node]
        mid = (lo + hi) // 2
        return self._query(2 * node, lo, mid, l, r) + self._query(2 * node + 1, mid + 1, hi, l, r)
