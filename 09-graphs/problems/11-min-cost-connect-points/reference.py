import heapq


def min_cost_connect(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 1:
        return 0
    in_tree = [False] * n
    total = 0
    pq: list[tuple[int, int]] = [(0, 0)]
    edges_added = 0
    while pq and edges_added < n:
        w, u = heapq.heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        total += w
        edges_added += 1
        for v in range(n):
            if not in_tree[v]:
                d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(pq, (d, v))
    return total
