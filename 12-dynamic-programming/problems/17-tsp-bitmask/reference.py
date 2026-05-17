def tsp(dist: list[list[int]]) -> int:
    n = len(dist)
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1, 1 << n):
        if not (mask & 1):
            continue
        for i in range(n):
            if not (mask >> i) & 1:
                continue
            cur = dp[mask][i]
            if cur == INF:
                continue
            for j in range(n):
                if (mask >> j) & 1 or i == j:
                    continue
                new_mask = mask | (1 << j)
                if cur + dist[i][j] < dp[new_mask][j]:
                    dp[new_mask][j] = cur + dist[i][j]
    full = (1 << n) - 1
    return int(min(dp[full][i] + dist[i][0] for i in range(1, n)))
