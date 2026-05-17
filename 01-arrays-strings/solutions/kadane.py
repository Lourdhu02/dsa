"""Kadane's algorithm — maximum-sum contiguous subarray."""

from __future__ import annotations


def kadane(xs: list[int]) -> int:
    """Maximum contiguous subarray sum.

    Empty array semantics: raises ValueError (the empty subarray would have
    sum 0 by convention but the LeetCode-style problem asks for non-empty).

    Time:  Θ(n)
    Space: Θ(1)
    Reference: Bentley, *Programming Pearls* (1986), §8.
    """
    if not xs:
        raise ValueError("xs must be non-empty")
    best = ending_here = xs[0]
    # Invariant: ending_here == max-sum contiguous subarray ending at index i-1.
    for x in xs[1:]:
        ending_here = max(x, ending_here + x)
        best = max(best, ending_here)
    return best
