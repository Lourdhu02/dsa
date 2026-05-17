def min_subarray_len(target: int, nums: list[int]) -> int:
    """Shrinking window over positive integers.

    Time:  Θ(n)
    Space: Θ(1)
    """
    n = len(nums)
    best = n + 1
    s = 0
    l = 0
    for r in range(n):
        s += nums[r]
        while s >= target:
            if r - l + 1 < best:
                best = r - l + 1
            s -= nums[l]
            l += 1
    return 0 if best == n + 1 else best
