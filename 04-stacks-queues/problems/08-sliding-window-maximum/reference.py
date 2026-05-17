from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Time: Θ(n).  Space: Θ(k)."""
    if k <= 0:
        return []
    dq: deque[int] = deque()
    out: list[int] = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
