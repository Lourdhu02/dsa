"""Hand-rolled sort implementations referenced by the lesson and the notebook."""

from __future__ import annotations


def insertion_sort(xs: list[int]) -> list[int]:
    """Stable in-place insertion sort.

    Time:  Θ(n) best, Θ(n²) worst.
    Space: Θ(1).
    """
    a = xs[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(xs: list[int]) -> list[int]:
    """Unstable in-place.  Always Θ(n²)."""
    a = xs[:]
    for i in range(len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def counting_sort(xs: list[int]) -> list[int]:
    """Stable, Θ(n + k) where k = value range.  Requires non-negative integers."""
    if not xs:
        return []
    if min(xs) < 0:
        raise ValueError("counting_sort requires non-negative ints")
    k = max(xs) + 1
    counts = [0] * k
    for x in xs:
        counts[x] += 1
    out: list[int] = []
    for v, c in enumerate(counts):
        out.extend([v] * c)
    return out
