def longest_palindrome(s: str) -> str:
    """Expand around each of the 2n-1 possible centers.

    Time:  Θ(n²)
    Space: Θ(1)
    """
    if not s:
        return ""
    best_l, best_r = 0, 0
    for i in range(len(s)):
        l1, r1 = _expand(s, i, i)
        l2, r2 = _expand(s, i, i + 1)
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2
    return s[best_l : best_r + 1]


def _expand(s: str, l: int, r: int) -> tuple[int, int]:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return l + 1, r - 1
