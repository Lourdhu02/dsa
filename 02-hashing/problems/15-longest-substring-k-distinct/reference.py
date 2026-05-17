from collections import defaultdict


def longest_at_most_k(s: str, k: int) -> int:
    """Variable-size sliding window.  Time: Θ(n).  Space: Θ(σ)."""
    if k <= 0:
        return 0
    counts: dict[str, int] = defaultdict(int)
    l = 0
    best = 0
    for r, ch in enumerate(s):
        counts[ch] += 1
        while len(counts) > k:
            counts[s[l]] -= 1
            if counts[s[l]] == 0:
                del counts[s[l]]
            l += 1
        if r - l + 1 > best:
            best = r - l + 1
    return best
