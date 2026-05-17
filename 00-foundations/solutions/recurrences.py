"""Master theorem applied programmatically.

Given coefficients ``a``, ``b``, and an exponent ``k`` such that
``f(n) = Θ(n^k)``, return a human-readable description of T(n).

This is purely educational: in real proofs we work the math out by hand and
quote CLRS § 4.5.  But mechanizing it is a useful exercise and lets the
tests check we got the case analysis right.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class MasterResult:
    case: int          # 1, 2 or 3
    bound: str         # e.g. "Theta(n^2 log n)"


def master_theorem(a: int, b: int, k: float) -> MasterResult:
    """Solve T(n) = a · T(n/b) + Θ(n^k), assuming a ≥ 1, b > 1, k ≥ 0.

    Time:  Θ(1)
    Space: Θ(1)

    Examples
    --------
    >>> master_theorem(2, 2, 1)        # merge sort
    MasterResult(case=2, bound='Theta(n^1 log n)')
    >>> master_theorem(2, 2, 0)        # binary search-shaped (just illustrative)
    MasterResult(case=1, bound='Theta(n^1)')
    >>> master_theorem(7, 2, 2)        # Strassen
    MasterResult(case=1, bound='Theta(n^2.807...)')
    """
    if a < 1:
        raise ValueError("a must be >= 1")
    if b <= 1:
        raise ValueError("b must be > 1")
    if k < 0:
        raise ValueError("k must be >= 0")

    log_b_a = math.log(a, b)

    # epsilon comparison with a tiny tolerance so floats don't bite us.
    eps = 1e-9
    if k < log_b_a - eps:
        # Case 1: f grows polynomially slower than n^(log_b a).
        return MasterResult(case=1, bound=f"Theta(n^{_fmt(log_b_a)})")
    if abs(k - log_b_a) <= eps:
        # Case 2 (k=0 form of the general k≥0 statement).
        return MasterResult(case=2, bound=f"Theta(n^{_fmt(log_b_a)} log n)")
    # Case 3: f grows polynomially faster.  The regularity condition is
    # automatically satisfied when f is a single polynomial term.
    return MasterResult(case=3, bound=f"Theta(n^{_fmt(k)})")


def _fmt(x: float) -> str:
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return f"{x:.3f}..."
