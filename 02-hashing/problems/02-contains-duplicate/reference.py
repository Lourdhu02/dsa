def contains_duplicate(nums: list[int]) -> bool:
    """Time: Θ(n) avg.  Space: Θ(n)."""
    seen: set[int] = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
