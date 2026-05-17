from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """Time: Θ(n).  Space: Θ(σ) where σ is alphabet size."""
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
