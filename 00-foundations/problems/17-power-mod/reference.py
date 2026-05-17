def pow_mod(a: int, n: int, m: int) -> int:
    """Modular exponentiation by repeated squaring.

    Time:  Θ(log n) multiplications, each on integers < m^2.
    Space: Θ(1).
    """
    if m <= 0:
        raise ValueError("m must be positive")
    if n < 0 or a < 0:
        raise ValueError("a and n must be non-negative")
    if m == 1:
        return 0
    result = 1
    base = a % m
    while n > 0:
        if n & 1:
            result = (result * base) % m
        base = (base * base) % m
        n >>= 1
    return result
