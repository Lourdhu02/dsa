def max_sum_k(nums: list[int], k: int) -> int:
    """Max sum of any contiguous subarray of length k.

    Time:  Θ(n)
    Space: Θ(1)
    """
    if k <= 0 or k > len(nums):
        raise ValueError("invalid k")
    window = sum(nums[:k])
    best = window
    for r in range(k, len(nums)):
        window += nums[r] - nums[r - k]
        if window > best:
            best = window
    return best
