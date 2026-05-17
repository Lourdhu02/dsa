def h_index(citations: list[int]) -> int:
    """Time: Θ(n).  Space: Θ(n)."""
    n = len(citations)
    buckets = [0] * (n + 1)
    for c in citations:
        buckets[min(c, n)] += 1
    total = 0
    for h in range(n, -1, -1):
        total += buckets[h]
        if total >= h:
            return h
    return 0
