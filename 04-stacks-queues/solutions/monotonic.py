"""Monotonic stack/deque templates used across the practice problems."""

from __future__ import annotations

from collections import deque


def next_greater_right(nums: list[int]) -> list[int]:
    """For each i, return the value of the first element to the right strictly greater than nums[i],
    or -1 if none.

    Time:  Θ(n) amortized (each index enters and leaves the stack once).
    Space: Θ(n).
    """
    n = len(nums)
    res = [-1] * n
    stack: list[int] = []  # indices, values nondecreasing from bottom to top
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    """Maximum of every length-k sliding window.

    Time:  Θ(n)
    Space: Θ(k)
    """
    if k <= 0 or k > len(nums):
        raise ValueError("invalid k")
    out: list[int] = []
    dq: deque[int] = deque()  # holds indices, values strictly decreasing
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
