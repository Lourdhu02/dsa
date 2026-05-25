def gcd(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("gcd is defined for only non-negative integers.")
    while b != 0:
        a, b = b, a % b
    return a

    # TODO: Euclidean algorithm.
    raise NotImplementedError
