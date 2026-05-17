import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    """Time: Θ(n log k).  Space: Θ(k)."""
    h: list[int] = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
