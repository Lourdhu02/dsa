"""Prefix-sum building block.  ``P[i] = sum(xs[:i])`` so ``sum(xs[l:r]) = P[r] - P[l]``."""

from __future__ import annotations


class PrefixSum:
    """1-D prefix-sum index.

    Build: Θ(n) time, Θ(n) space.
    Query ``range_sum(l, r)``: Θ(1).
    """

    def __init__(self, xs: list[int]) -> None:
        n = len(xs)
        # P[0] = 0 sentinel so range_sum(0, k) works without a special case.
        self._p: list[int] = [0] * (n + 1)
        for i, x in enumerate(xs):
            self._p[i + 1] = self._p[i] + x

    def range_sum(self, l: int, r: int) -> int:
        """Return ``sum(xs[l:r])``.  Half-open interval; r > l."""
        if l < 0 or r > len(self._p) - 1 or l > r:
            raise IndexError(f"invalid range [{l}, {r})")
        return self._p[r] - self._p[l]
