"""Pure-Python implementations of the standard growth functions plotted in this
module's notebook.  We keep them naive on purpose so the operation count is
obvious from the source.
"""

from __future__ import annotations


def constant_ops(n: int) -> int:
    """Always does the same amount of work regardless of ``n``.

    Time:  Θ(1)
    Space: Θ(1)
    """
    _ = n  # silence linters
    return 1


def log_ops(n: int) -> int:
    """Halve until 1.  Used to illustrate Θ(log n) — binary search shape.

    Time:  Θ(log n)
    Space: Θ(1)
    """
    if n < 1:
        return 0
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count


def linear_ops(n: int) -> int:
    """Single pass.

    Time:  Θ(n)
    Space: Θ(1)
    """
    count = 0
    for _ in range(n):
        count += 1
    return count


def n_log_n_ops(n: int) -> int:
    """n outer steps, log n inner.

    Time:  Θ(n log n)
    Space: Θ(1)
    """
    count = 0
    for _ in range(n):
        m = max(n, 1)
        while m > 1:
            m //= 2
            count += 1
    return count


def quadratic_ops(n: int) -> int:
    """Nested loop.

    Time:  Θ(n²)
    Space: Θ(1)
    """
    count = 0
    for _ in range(n):
        for _ in range(n):
            count += 1
    return count


def exponential_ops(n: int) -> int:
    """2^n branching — only safe to call for n ≤ ~25.

    Time:  Θ(2^n)
    Space: Θ(n) (call stack depth)
    """
    if n <= 0:
        return 1
    return exponential_ops(n - 1) + exponential_ops(n - 1)
