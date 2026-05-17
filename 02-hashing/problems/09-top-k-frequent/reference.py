from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Bucket sort by frequency for guaranteed Θ(n).

    Time:  Θ(n).  Space: Θ(n).
    """
    counts = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)
    out: list[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for v in buckets[freq]:
            out.append(v)
            if len(out) == k:
                return out
    return out
