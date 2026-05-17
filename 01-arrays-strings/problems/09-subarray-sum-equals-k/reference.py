from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    """Count subarrays summing to k via prefix-sum frequency table.

    Time:  Θ(n)
    Space: Θ(n) for the hash map.
    """
    count = defaultdict(int)
    count[0] = 1
    cur = 0
    total = 0
    for x in nums:
        cur += x
        total += count[cur - k]
        count[cur] += 1
    return total
