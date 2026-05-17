"""Backtracking templates (permutations, combinations, subsets)."""

from __future__ import annotations


def permutations(nums: list[int]) -> list[list[int]]:
    """All permutations of a list of distinct ints.

    Time: Θ(n · n!).  Space: Θ(n) recursion + output.
    """
    out: list[list[int]] = []
    used = [False] * len(nums)
    path: list[int] = []

    def _bt() -> None:
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            _bt()
            path.pop()
            used[i] = False

    _bt()
    return out


def combinations(n: int, k: int) -> list[list[int]]:
    """All k-element subsets of {1..n}.

    Time: Θ(C(n, k) · k).  Space: Θ(k) recursion.
    """
    out: list[list[int]] = []
    path: list[int] = []

    def _bt(start: int) -> None:
        if len(path) == k:
            out.append(path[:])
            return
        # Pruning: need (k - len(path)) more items, available = n - start + 1.
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            _bt(i + 1)
            path.pop()

    _bt(1)
    return out
