"""Mergesort, quicksort, and quickselect implementations referenced by problems."""

from __future__ import annotations

import random


def merge_sort(xs: list[int]) -> list[int]:
    """Stable mergesort.

    Time:  Θ(n log n) all cases.
    Space: Θ(n) auxiliary (the merge buffers).
    Reference: CLRS § 2.3.
    """
    if len(xs) <= 1:
        return xs[:]
    mid = len(xs) // 2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])
    return _merge(left, right)


def _merge(a: list[int], b: list[int]) -> list[int]:
    out: list[int] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # `<=` keeps the sort stable: a's element wins ties, preserving original order.
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out


def quick_sort(xs: list[int]) -> list[int]:
    """In-place quicksort with random pivot.

    Time:  Θ(n log n) expected (random pivot), Θ(n²) worst.
    Space: Θ(log n) expected stack depth.
    Reference: Hoare (1962); CLRS § 7.
    """
    a = xs[:]
    _qs(a, 0, len(a) - 1)
    return a


def _qs(a: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    p = _partition(a, lo, hi)
    _qs(a, lo, p - 1)
    _qs(a, p + 1, hi)


def _partition(a: list[int], lo: int, hi: int) -> int:
    # Random pivot to avoid Θ(n²) on sorted/adversarial inputs.
    pivot_idx = random.randint(lo, hi)
    a[pivot_idx], a[hi] = a[hi], a[pivot_idx]
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


def quickselect(xs: list[int], k: int) -> int:
    """Return the k-th smallest element (0-indexed) without sorting the whole list.

    Time:  Θ(n) expected, Θ(n²) worst.  Median-of-medians achieves Θ(n) worst
           but with higher constants (CLRS § 9.3).
    Space: Θ(log n) expected stack depth.
    """
    if not 0 <= k < len(xs):
        raise IndexError(k)
    a = xs[:]
    lo, hi = 0, len(a) - 1
    while lo < hi:
        p = _partition(a, lo, hi)
        if p == k:
            return a[p]
        if p < k:
            lo = p + 1
        else:
            hi = p - 1
    return a[k]
