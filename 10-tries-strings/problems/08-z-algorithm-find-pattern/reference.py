def z_function(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def z_find(text: str, pat: str) -> list[int]:
    if not pat:
        return list(range(len(text) + 1))
    combined = pat + "$" + text
    z = z_function(combined)
    out: list[int] = []
    m = len(pat)
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            out.append(i - m - 1)
    return out
