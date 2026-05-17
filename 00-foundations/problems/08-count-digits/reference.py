def count_digits(n: int) -> int:
    """Count decimal digits of a non-negative integer.

    Time:  Θ(log10 n)
    Space: Θ(1)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    count = 0
    while n:
        n //= 10
        count += 1
    return count
