def popcount(n: int) -> int:
    """Hamming weight via Brian Kernighan's trick.

    ``n & (n - 1)`` clears the lowest set bit.  So the loop runs once per
    set bit, not once per total bit.

    Time:  Θ(k) where k is the number of set bits.
    Space: Θ(1).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
