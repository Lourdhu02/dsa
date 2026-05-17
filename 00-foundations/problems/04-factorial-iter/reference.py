def factorial(n: int) -> int:
    """Iterative factorial.

    Time:  Θ(n) multiplications.  Each multiplication is on bignum integers
           whose width grows like Θ(n log n) bits (Stirling), so total bit
           operations are super-linear; for pure Θ analysis over the word RAM
           we still write Θ(n).
    Space: Θ(1) ignoring the size of the output.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    # Invariant: at the start of iteration i, result == (i-1)!.
    for i in range(2, n + 1):
        result *= i
    return result
