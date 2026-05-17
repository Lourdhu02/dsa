"""The four binary-search variants in one place.  All use the same invariant pattern."""

from __future__ import annotations

from typing import Callable


def search_exact(a: list[int], target: int) -> int:
    """Return index of target in sorted ``a``, or -1 if absent.

    Time: Θ(log n).  Space: Θ(1).
    """
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(a: list[int], target: int) -> int:
    """Smallest index ``i`` such that ``a[i] >= target``.  If none, returns ``len(a)``.

    Equivalent to ``bisect.bisect_left(a, target)``.
    """
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(a: list[int], target: int) -> int:
    """Smallest index ``i`` such that ``a[i] > target``.

    Equivalent to ``bisect.bisect_right(a, target)``.
    """
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def first_true(lo: int, hi: int, predicate: Callable[[int], bool]) -> int:
    """Smallest x in [lo, hi] with ``predicate(x)`` True, assuming monotone:
    once True, always True.  Returns ``hi + 1`` if no such x.

    Useful for "binary search on the answer" problems.

    Time: Θ(log(hi - lo) * cost(predicate)).
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo if predicate(lo) else lo + 1
