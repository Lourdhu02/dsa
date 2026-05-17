"""KMP failure function and match.  Reference: Knuth, Morris & Pratt (1977)."""

from __future__ import annotations


def build_failure(pat: str) -> list[int]:
    """Failure / longest-proper-prefix-suffix table.  Time: Θ(m).  Space: Θ(m)."""
    f = [0] * len(pat)
    k = 0
    for i in range(1, len(pat)):
        while k and pat[k] != pat[i]:
            k = f[k - 1]
        if pat[k] == pat[i]:
            k += 1
        f[i] = k
    return f


def kmp_find_all(text: str, pat: str) -> list[int]:
    """All starting indices of ``pat`` in ``text``.  Time: Θ(n + m)."""
    if not pat:
        return list(range(len(text) + 1))
    f = build_failure(pat)
    out: list[int] = []
    k = 0
    for i, ch in enumerate(text):
        while k and pat[k] != ch:
            k = f[k - 1]
        if pat[k] == ch:
            k += 1
        if k == len(pat):
            out.append(i - len(pat) + 1)
            k = f[k - 1]
    return out
