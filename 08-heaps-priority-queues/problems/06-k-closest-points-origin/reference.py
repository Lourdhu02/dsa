import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    h: list[tuple[int, list[int]]] = []
    for p in points:
        d = p[0] * p[0] + p[1] * p[1]
        if len(h) < k:
            heapq.heappush(h, (-d, p))
        elif -d > h[0][0]:
            heapq.heapreplace(h, (-d, p))
    return [p for _, p in h]
