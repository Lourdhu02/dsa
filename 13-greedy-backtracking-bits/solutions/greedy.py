"""Greedy templates referenced by the practice problems."""

from __future__ import annotations


def activity_selection(intervals: list[tuple[int, int]]) -> int:
    """Maximum non-overlapping subset of intervals.

    Greedy: sort by END time, take the earliest-ending compatible interval.
    Time: Θ(n log n).  Reference: CLRS § 16.1.
    """
    if not intervals:
        return 0
    by_end = sorted(intervals, key=lambda x: x[1])
    count = 1
    last_end = by_end[0][1]
    for s, e in by_end[1:]:
        if s >= last_end:
            count += 1
            last_end = e
    return count
