def three_sum(nums: list[int]) -> list[list[int]]:
    """Sort + two-pointer.

    Time:  Θ(n²)
    Space: Θ(1) extra (or Θ(n) counting sort scratch).
    """
    nums = sorted(nums)
    n = len(nums)
    out: list[list[int]] = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return out
