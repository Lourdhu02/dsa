def max_product(nums: list[int]) -> int:
    best = lo = hi = nums[0]
    for x in nums[1:]:
        candidates = (x, hi * x, lo * x)
        hi = max(candidates)
        lo = min(candidates)
        if hi > best:
            best = hi
    return best
