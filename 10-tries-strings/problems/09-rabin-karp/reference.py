def rabin_karp(text: str, pat: str) -> list[int]:
    n, m = len(text), len(pat)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    BASE, MOD = 257, (1 << 61) - 1
    pat_h = 0
    win_h = 0
    high = pow(BASE, m - 1, MOD)
    for i in range(m):
        pat_h = (pat_h * BASE + ord(pat[i])) % MOD
        win_h = (win_h * BASE + ord(text[i])) % MOD
    out: list[int] = []
    for i in range(n - m + 1):
        if win_h == pat_h and text[i : i + m] == pat:
            out.append(i)
        if i + m < n:
            win_h = ((win_h - ord(text[i]) * high) * BASE + ord(text[i + m])) % MOD
    return out
