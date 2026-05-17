def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    f = [0] * len(needle)
    k = 0
    for i in range(1, len(needle)):
        while k and needle[k] != needle[i]:
            k = f[k - 1]
        if needle[k] == needle[i]:
            k += 1
        f[i] = k
    k = 0
    for i, ch in enumerate(haystack):
        while k and needle[k] != ch:
            k = f[k - 1]
        if needle[k] == ch:
            k += 1
        if k == len(needle):
            return i - len(needle) + 1
    return -1
