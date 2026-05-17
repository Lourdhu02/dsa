def length_of_longest_substring(s: str) -> int:
    """Variable-size sliding window over characters.

    Time:  Θ(n).  Each character enters and leaves the set at most once;
           total work across the whole loop is therefore Θ(n) amortized.
    Space: Θ(min(n, σ)) where σ is the alphabet.
    """
    seen: set[str] = set()
    best = 0
    l = 0
    for r, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[l])
            l += 1
        seen.add(ch)
        if r - l + 1 > best:
            best = r - l + 1
    return best
