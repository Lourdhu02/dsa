def majority_element(nums: list[int]) -> int:
    def _rec(lo: int, hi: int) -> int:
        if lo == hi:
            return nums[lo]
        mid = (lo + hi) // 2
        left = _rec(lo, mid)
        right = _rec(mid + 1, hi)
        if left == right:
            return left
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
        return left if left_count > right_count else right

    return _rec(0, len(nums) - 1)
