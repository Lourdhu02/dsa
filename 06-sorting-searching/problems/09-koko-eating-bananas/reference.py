def min_eating_speed(piles: list[int], h: int) -> int:
    def hours(k: int) -> int:
        return sum(-(-p // k) for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
