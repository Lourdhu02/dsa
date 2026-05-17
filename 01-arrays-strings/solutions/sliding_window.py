"""Generic sliding-window templates."""

from __future__ import annotations

from typing import Callable


def fixed_window_max_sum(xs: list[int], k: int) -> int:
    """Maximum sum of any contiguous subarray of length exactly k.

    Time:  Θ(n)
    Space: Θ(1)
    """
    if k <= 0 or k > len(xs):
        raise ValueError("k must satisfy 1 <= k <= len(xs)")
    window = sum(xs[:k])
    best = window
    # Invariant: window == sum(xs[r-k+1..r]) at the top of iteration r.
    for r in range(k, len(xs)):
        window += xs[r] - xs[r - k]
        if window > best:
            best = window
    return best


def variable_window_min_length(
    xs: list[int],
    is_valid: Callable[[int, int, int], bool],
    add: Callable[[int, int], int],
    remove: Callable[[int, int], int],
) -> int:
    """Generic skeleton — caller supplies how the window's *state* is updated.

    Returns the length of the shortest valid window, or 0 if none exists.

    Time:  Θ(n) amortized (l advances at most n times across all iterations).
    Space: Θ(1) ignoring the closures' capture.
    """
    n = len(xs)
    state = 0
    l = 0
    best = n + 1
    for r in range(n):
        state = add(state, xs[r])
        while is_valid(state, l, r):
            best = min(best, r - l + 1)
            state = remove(state, xs[l])
            l += 1
    return 0 if best == n + 1 else best
