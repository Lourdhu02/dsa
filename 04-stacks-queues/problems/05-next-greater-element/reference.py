def next_greater(nums: list[int]) -> list[int]:
    """Time: Θ(n) amortized.  Space: Θ(n)."""
    n = len(nums)
    res = [-1] * n
    stack: list[int] = []
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res
