def reverse_string(s: list[str]) -> None:
    """Two-pointer in-place reverse.

    Time:  Θ(n)
    Space: Θ(1)
    """
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
