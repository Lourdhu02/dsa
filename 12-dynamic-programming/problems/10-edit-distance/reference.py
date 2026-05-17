def min_distance(s: str, t: str) -> int:
    if len(s) < len(t):
        s, t = t, s
    prev = list(range(len(t) + 1))
    cur = [0] * (len(t) + 1)
    for i, sc in enumerate(s, start=1):
        cur[0] = i
        for j, tc in enumerate(t, start=1):
            if sc == tc:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
        prev, cur = cur, prev
    return prev[len(t)]
