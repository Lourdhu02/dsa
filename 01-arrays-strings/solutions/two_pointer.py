"""Canonical two-pointer templates referenced by the practice problems."""

from __future__ import annotations


def converging(xs: list[int], target: int) -> tuple[int, int] | None:
    """Find indices (i, j) with i < j and xs[i] + xs[j] == target on a SORTED array.

    Time:  Θ(n)
    Space: Θ(1)
    """
    lo, hi = 0, len(xs) - 1
    # Invariant: every pair we have NOT examined lies within [lo, hi].
    while lo < hi:
        s = xs[lo] + xs[hi]
        if s == target:
            return lo, hi
        if s < target:
            lo += 1
        else:
            hi -= 1
    return None


def same_direction_compact(xs: list[int], keep) -> int:
    """In-place compaction: keep elements where ``keep(x)`` is True.

    Returns the new length.  The first ``new_length`` slots of ``xs`` hold the
    surviving elements in their original order; the rest of ``xs`` is unspecified.

    Time:  Θ(n)
    Space: Θ(1)
    """
    write = 0
    for read in range(len(xs)):
        if keep(xs[read]):
            xs[write] = xs[read]
            write += 1
    return write
