def palindrome_pairs(words: list[str]) -> list[list[int]]:
    index = {w: i for i, w in enumerate(words)}
    out: list[list[int]] = []

    def _is_pal(s: str) -> bool:
        return s == s[::-1]

    for i, w in enumerate(words):
        for k in range(len(w) + 1):
            pref, suf = w[:k], w[k:]
            if _is_pal(pref):
                rev_suf = suf[::-1]
                if rev_suf != w and rev_suf in index:
                    out.append([index[rev_suf], i])
            if k != len(w) and _is_pal(suf):
                rev_pref = pref[::-1]
                if rev_pref != w and rev_pref in index:
                    out.append([i, index[rev_pref]])
    return out
