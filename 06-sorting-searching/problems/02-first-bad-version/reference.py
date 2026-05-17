from typing import Callable


def first_bad_version(n: int, is_bad: Callable[[int], bool]) -> int:
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if is_bad(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
