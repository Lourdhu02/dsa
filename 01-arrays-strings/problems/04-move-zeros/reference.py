def move_zeros(nums: list[int]) -> None:
    """Swap non-zeros forward; remaining slots fill with zeros.

    Time:  Θ(n)
    Space: Θ(1)
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
