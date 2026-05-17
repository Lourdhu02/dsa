def isqrt(n: int) -> int:
    """Floor of sqrt(n) by binary search.

    Time:  Θ(log n) iterations, each doing one bignum multiplication.
    Space: Θ(1).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    lo, hi = 1, n
    # Invariant: lo*lo <= n  and  every r > hi has r*r > n.
    # Equivalently: the answer is in [lo, hi].
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == n:
            return mid
        if sq < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi
