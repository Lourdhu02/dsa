import random


def kth_smallest(nums: list[int], k: int) -> int:
    a = nums[:]
    target = k - 1
    lo, hi = 0, len(a) - 1
    while lo < hi:
        pi = random.randint(lo, hi)
        a[pi], a[hi] = a[hi], a[pi]
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        if i == target:
            return a[i]
        if i < target:
            lo = i + 1
        else:
            hi = i - 1
    return a[target]
