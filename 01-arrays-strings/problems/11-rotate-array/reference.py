def rotate(nums: list[int], k: int) -> None:
    """In-place right rotation by k using triple-reverse.

    Time:  Θ(n)
    Space: Θ(1)
    """
    n = len(nums)
    if n == 0:
        return
    k %= n
    _reverse(nums, 0, n - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, n - 1)


def _reverse(a: list[int], i: int, j: int) -> None:
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
