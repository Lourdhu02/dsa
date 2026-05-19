def fib(n: int) -> int:
    prev = 0
    curr = 1
    if n < 0:
        raise ValueError("Enter non negative numbers")
    for i in range(1, n + 1):
        (prev, curr) = (curr, prev + curr)
    return prev
    # TODO: iterative, carrying only the last two values.
    raise NotImplementedError
