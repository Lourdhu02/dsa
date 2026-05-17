def reverse_bits_32(n: int) -> int:
    """Reverse the lowest 32 bits of n.

    Time:  Θ(1) — exactly 32 iterations.
    Space: Θ(1).
    """
    if n < 0 or n >= (1 << 32):
        raise ValueError("n must be in [0, 2^32)")
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
