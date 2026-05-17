"""Reference solutions."""


def sum_to_n_loop(n: int) -> int:
    """Linear-time accumulation.

    Time:  Θ(n)
    Space: Θ(1)
    """
    total = 0
    # Invariant: at the top of iteration i, total == sum(1..i-1).
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_formula(n: int) -> int:
    """Closed form (Gauss's pairing trick).

    Time:  Θ(1)
    Space: Θ(1)
    """
    return n * (n + 1) // 2
