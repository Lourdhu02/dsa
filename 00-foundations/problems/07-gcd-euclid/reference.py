def gcd(a: int, b: int) -> int:
    """Euclidean algorithm, iterative form.

    Time:  Θ(log min(a, b)).  Worst case is Fibonacci pair (Lamé 1844).
    Space: Θ(1).
    """
    if a < 0 or b < 0:
        raise ValueError("inputs must be non-negative")
    while b:
        a, b = b, a % b
    return a
