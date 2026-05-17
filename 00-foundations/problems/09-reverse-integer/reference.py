def reverse_integer(n: int) -> int:
    """Reverse decimal digits, preserving sign.

    Time:  Θ(d) where d = number of digits.
    Space: Θ(1).
    """
    sign = -1 if n < 0 else 1
    n = abs(n)
    result = 0
    while n:
        result = result * 10 + n % 10
        n //= 10
    return sign * result
