def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """One-pass hash map.

    Time:  Θ(n) average (hash lookup), Θ(n²) adversarial worst.
    Space: Θ(n).
    """
    seen: dict[int, int] = {}
    for j, x in enumerate(nums):
        if target - x in seen:
            return seen[target - x], j
        seen[x] = j
    raise ValueError("no solution")
