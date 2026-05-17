"""Bit manipulation helpers."""

from __future__ import annotations


def lowest_set_bit(x: int) -> int:
    """Returns 2^i where i is the lowest set bit of x.  0 if x == 0."""
    return x & -x


def clear_lowest_set_bit(x: int) -> int:
    return x & (x - 1)


def iter_submasks(mask: int):
    """Iterate all non-empty submasks of ``mask`` in descending order."""
    s = mask
    while s:
        yield s
        s = (s - 1) & mask
