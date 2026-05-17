def shortest_palindrome(s: str) -> str:
    combined = s + "#" + s[::-1]
    f = [0] * len(combined)
    k = 0
    for i in range(1, len(combined)):
        while k and combined[k] != combined[i]:
            k = f[k - 1]
        if combined[k] == combined[i]:
            k += 1
        f[i] = k
    longest_pal_prefix = f[-1]
    return s[longest_pal_prefix:][::-1] + s
