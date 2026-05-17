def search_range(nums: list[int], target: int) -> list[int]:
    def lb(t):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    left = lb(target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = lb(target + 1) - 1
    return [left, right]
