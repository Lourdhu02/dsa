"""Reference DP templates: 0/1 knapsack, unbounded knapsack, LIS, edit distance."""

from __future__ import annotations

from bisect import bisect_left


def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """0/1 knapsack — each item used at most once.

    Time:  Θ(n · capacity).  Space: Θ(capacity) via 1D rolling array.
    """
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):
            if dp[c - w] + v > dp[c]:
                dp[c] = dp[c - w] + v
    return dp[capacity]


def knapsack_unbounded(weights: list[int], values: list[int], capacity: int) -> int:
    """Unbounded — each item usable any number of times.

    Time:  Θ(n · capacity).  Space: Θ(capacity).
    """
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(w, capacity + 1):
            if dp[c - w] + v > dp[c]:
                dp[c] = dp[c - w] + v
    return dp[capacity]


def lis_length(nums: list[int]) -> int:
    """Length of the longest STRICTLY increasing subsequence.

    Time:  Θ(n log n) via patience sorting.
    Space: Θ(n).
    """
    tails: list[int] = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def edit_distance(s: str, t: str) -> int:
    """Levenshtein distance — min insertions/deletions/substitutions.

    Time:  Θ(n · m).  Space: Θ(min(n, m)).
    """
    if len(s) < len(t):
        s, t = t, s
    prev = list(range(len(t) + 1))
    cur = [0] * (len(t) + 1)
    for i, sc in enumerate(s, start=1):
        cur[0] = i
        for j, tc in enumerate(t, start=1):
            if sc == tc:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
        prev, cur = cur, prev
    return prev[len(t)]
