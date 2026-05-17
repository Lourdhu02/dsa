"""Starter — implement both versions."""


def sum_to_n_loop(n: int) -> int:
    sum = 0
    if n >= 0:
        for i in range(1, n + 1):
            sum += i
        return sum
    raise NotImplementedError


def sum_to_n_formula(n: int) -> int:
    sum = 0
    if n >= 0:
        sum = (n * (n + 1)) // 2
        return sum
    # TODO: closed form, Θ(1).
    raise NotImplementedError
