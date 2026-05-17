def factorial(n: int) -> int:
    """Time: Θ(n).  Space: Θ(n) stack."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)
