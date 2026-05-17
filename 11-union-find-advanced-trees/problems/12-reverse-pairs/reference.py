from bisect import bisect_left


def reverse_pairs(nums: list[int]) -> int:
    sorted_unique = sorted(set(nums + [2 * x for x in nums]))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    n = len(sorted_unique)
    bit = [0] * (n + 2)

    def update(i):
        while i <= n:
            bit[i] += 1
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    count = 0
    for x in reversed(nums):
        # count of seen values y where y < x / 2 strictly, i.e., 2y < x.
        idx = bisect_left(sorted_unique, x) + 1  # rank of x in sorted_unique (>=1)
        # We want y such that x > 2*y, i.e., 2*y < x.  rank of largest 2*y < x:
        target_idx = bisect_left(sorted_unique, x) + 1  # placeholder; recompute via 2*y
        # number of seen entries with value strictly less than x/2 (i.e. 2*value < x).
        # We track by value rank in BIT.
        thr_idx = bisect_left(sorted_unique, (x + 1) // 2 if x % 2 else x // 2)
        # We want indices with value < ceil(x/2). For real x, condition is value*2 < x i.e. value < x/2.
        # Equivalently among integers value <= (x-1)//2 if x integer.
        thr = (x - 1) // 2 if x > 0 else (x // 2) - 1
        thr_rank = bisect_left(sorted_unique, thr + 1)  # count of sorted_unique values <= thr
        count += prefix(thr_rank)
        update(rank[x])
    return count
