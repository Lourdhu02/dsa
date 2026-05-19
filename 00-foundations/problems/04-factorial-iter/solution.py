def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0 & 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
    # TODO: iterative product from 1 to n.
    raise NotImplementedError
