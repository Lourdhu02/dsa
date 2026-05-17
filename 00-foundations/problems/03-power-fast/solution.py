"""Starter."""


def power_linear(a: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            a *= a
    return a
    # TODO: multiply ``a`` by itself ``n`` times. Handle n == 0.
    raise NotImplementedError


def power_fast(a: int, n: int) -> int:
    # TODO: exponentiation by squaring — Θ(log n) multiplications.
    raise NotImplementedError
