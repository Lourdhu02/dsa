from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Bucket by sorted-character key.

    Time:  Θ(N · L log L) where N = number of strings, L = max length.
    Space: Θ(N · L).
    """
    buckets: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for s in strs:
        buckets[tuple(sorted(s))].append(s)
    return list(buckets.values())
