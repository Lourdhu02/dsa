def remove_duplicates(nums: list[int]) -> int:
    """In-place dedup of a sorted array.

    Time:  Θ(n)
    Space: Θ(1)
    """
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
