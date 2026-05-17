def is_happy(n: int) -> bool:
    """Time: Θ(log n) digits per step, bounded number of steps (the squared-digit
    sum has fixed points and short cycles).
    Space: Θ(k) for the seen set, k tiny in practice.
    """
    seen: set[int] = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
