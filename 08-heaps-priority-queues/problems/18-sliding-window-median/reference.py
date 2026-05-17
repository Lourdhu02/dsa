import heapq
from collections import defaultdict


def median_sliding_window(nums: list[int], k: int) -> list[float]:
    """Two heaps with lazy deletion.  Time: Θ(n log k)."""
    lo: list[int] = []  # max-heap, negated
    hi: list[int] = []  # min-heap
    removed: dict[int, int] = defaultdict(int)
    lo_size = hi_size = 0

    def _balance():
        # Ensure |lo| - |hi| in {0, 1}.
        nonlocal lo_size, hi_size
        while lo_size > hi_size + 1:
            v = -heapq.heappop(lo)
            heapq.heappush(hi, v)
            lo_size -= 1
            hi_size += 1
            while lo and removed[-lo[0]] > 0:
                removed[-lo[0]] -= 1
                heapq.heappop(lo)
        while hi_size > lo_size:
            v = heapq.heappop(hi)
            heapq.heappush(lo, -v)
            hi_size -= 1
            lo_size += 1
            while hi and removed[hi[0]] > 0:
                removed[hi[0]] -= 1
                heapq.heappop(hi)

    def _prune_tops():
        while lo and removed[-lo[0]] > 0:
            removed[-lo[0]] -= 1
            heapq.heappop(lo)
        while hi and removed[hi[0]] > 0:
            removed[hi[0]] -= 1
            heapq.heappop(hi)

    def _median():
        _prune_tops()
        if k % 2 == 1:
            return float(-lo[0])
        return (-lo[0] + hi[0]) / 2.0

    out: list[float] = []
    for i, x in enumerate(nums):
        if not lo or x <= -lo[0]:
            heapq.heappush(lo, -x)
            lo_size += 1
        else:
            heapq.heappush(hi, x)
            hi_size += 1
        _balance()
        if i >= k:
            old = nums[i - k]
            removed[old] += 1
            if old <= -lo[0]:
                lo_size -= 1
            else:
                hi_size -= 1
            _balance()
        if i >= k - 1:
            out.append(_median())
    return out
