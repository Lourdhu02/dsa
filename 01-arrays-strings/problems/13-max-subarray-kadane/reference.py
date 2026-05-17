def max_subarray(nums: list[int]) -> int:
    """Kadane's algorithm.

    Time:  Θ(n)
    Space: Θ(1)
    Reference: Bentley, *Programming Pearls* (1986), §8.
    """
    if not nums:
        raise ValueError("nums must be non-empty")
    best = ending_here = nums[0]
    for x in nums[1:]:
        ending_here = max(x, ending_here + x)
        if ending_here > best:
            best = ending_here
    return best
