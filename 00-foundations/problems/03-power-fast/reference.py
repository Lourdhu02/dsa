"""Reference solutions.

The two solutions differ only in their multiplication count.  Both compute
the same value in exact integer arithmetic (Python ints are arbitrary
precision, so no overflow concerns).
"""


def power_linear(a: int, n: int) -> int:
    """Naive repeated multiplication.

    Time:  Θ(n)
    Space: Θ(1)
    """
    result = 1
    # Invariant: after iteration i, result == a^i.
    for _ in range(n):
        result *= a
    return result


def power_fast(a: int, n: int) -> int:
    """Exponentiation by squaring.

    Reads the bits of n from low to high and squares the running base.

    Time:  Θ(log n)
    Space: Θ(1)
    Reference: CLRS 4th ed. § 31.6 (modular exponentiation has the same
    structure).
    """
    result = 1
    base = a
    while n > 0:
        if n & 1:
            result *= base
        base *= base
        n >>= 1
    return result
