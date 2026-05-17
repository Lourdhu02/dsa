def longest_consecutive(nums: list[int]) -> int:
    """Time: Θ(n) avg; each element visited at most twice.  Space: Θ(n)."""
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 in s:
            continue
        cur = x
        length = 1
        while cur + 1 in s:
            cur += 1
            length += 1
        if length > best:
            best = length
    return best
