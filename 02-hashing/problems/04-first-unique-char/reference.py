from collections import Counter


def first_uniq_char(s: str) -> int:
    """Time: Θ(n).  Space: Θ(σ)."""
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
