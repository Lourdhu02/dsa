def split_array(nums: list[int], k: int) -> int:
    def feasible(x: int) -> bool:
        parts = 1
        cur = 0
        for v in nums:
            if cur + v > x:
                parts += 1
                cur = v
            else:
                cur += v
        return parts <= k

    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
