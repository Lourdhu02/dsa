def is_power_of_two(n: int) -> bool:
    """Constant-time bit trick.

    Time:  Θ(1)
    Space: Θ(1)
    """
    return n > 0 and (n & (n - 1)) == 0
