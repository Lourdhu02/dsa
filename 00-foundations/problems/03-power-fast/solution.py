"""Starter."""

from unittest import result


def power_linear(a: int, n: int) -> int:
    result = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            result *= a
    return result
    # TODO: multiply ``a`` by itself ``n`` times. Handle n == 0.
    raise NotImplementedError


def power_fast(a: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            half = power_fast(a, (n // 2))
            result = half * half
        else:
            odd = power_fast(a, n - 1)
            result = a * odd
    return result

    return result

    # TODO: exponentiation by squaring — Θ(log n) multiplications.
    raise NotImplementedError
