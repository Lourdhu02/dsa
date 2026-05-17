def power(a: float, n: int) -> float:
    """Time: Θ(log |n|).  Space: Θ(log |n|) stack."""
    if n < 0:
        return 1.0 / power(a, -n)
    if n == 0:
        return 1.0
    half = power(a, n // 2)
    return half * half if n % 2 == 0 else half * half * a
