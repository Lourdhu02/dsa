def rob_circular(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def _rob(arr):
        prev = curr = 0
        for x in arr:
            prev, curr = curr, max(curr, prev + x)
        return curr

    return max(_rob(nums[:-1]), _rob(nums[1:]))
