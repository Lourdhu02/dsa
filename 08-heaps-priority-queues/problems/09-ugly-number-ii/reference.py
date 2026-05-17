import heapq


def nth_ugly(n: int) -> int:
    h = [1]
    seen = {1}
    cur = 1
    for _ in range(n):
        cur = heapq.heappop(h)
        for p in (2, 3, 5):
            nxt = cur * p
            if nxt not in seen:
                seen.add(nxt)
                heapq.heappush(h, nxt)
    return cur
