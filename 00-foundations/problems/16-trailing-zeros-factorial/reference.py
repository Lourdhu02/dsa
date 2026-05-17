def trailing_zeros(n: int) -> int:
    """Legendre's formula: count multiplicity of 5 in n!.

    Time:  Θ(log_5 n)
    Space: Θ(1)
    Reference: Legendre 1830; see https://en.wikipedia.org/wiki/Legendre%27s_formula
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    count = 0
    while n:
        n //= 5
        count += n
    return count
