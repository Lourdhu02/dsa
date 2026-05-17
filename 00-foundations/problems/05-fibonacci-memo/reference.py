from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Memoized recursive Fibonacci.

    Time:  Θ(n)  -- each fib(i) for 0..n is computed once.
    Space: Θ(n)  -- recursion depth and cache size.

    With Python's default recursion limit of 1000, this works up to n ≈ 990.
    Beyond that switch to the iterative form (problem 06).
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
