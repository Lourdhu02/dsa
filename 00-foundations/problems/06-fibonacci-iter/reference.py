def fib(n: int) -> int:
    """Iterative Fibonacci with constant extra space.

    Time:  Θ(n) ignoring bignum cost.
    Space: Θ(1).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    prev, curr = 0, 1
    # Invariant: at the top of iteration i (starting at 2), curr == fib(i-1) and prev == fib(i-2).
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
