import random


def quick_sort(xs: list[int]) -> list[int]:
    """Time: Θ(n log n) expected, Θ(n²) worst.  Space: Θ(log n) avg stack."""
    def _partition(lo: int, hi: int) -> int:
        pi = random.randint(lo, hi)
        xs[pi], xs[hi] = xs[hi], xs[pi]
        pivot = xs[hi]
        i = lo
        for j in range(lo, hi):
            if xs[j] < pivot:
                xs[i], xs[j] = xs[j], xs[i]
                i += 1
        xs[i], xs[hi] = xs[hi], xs[i]
        return i

    def _qs(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        p = _partition(lo, hi)
        _qs(lo, p - 1)
        _qs(p + 1, hi)

    _qs(0, len(xs) - 1)
    return xs
