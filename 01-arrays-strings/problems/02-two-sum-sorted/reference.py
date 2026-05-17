def two_sum_sorted(numbers: list[int], target: int) -> tuple[int, int]:
    """Converging two-pointer.

    Time:  Θ(n)
    Space: Θ(1)
    """
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        s = numbers[lo] + numbers[hi]
        if s == target:
            return lo + 1, hi + 1
        if s < target:
            lo += 1
        else:
            hi -= 1
    raise ValueError("no solution")
