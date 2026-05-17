def swim_in_water(grid: list[list[int]]) -> int:
    n = len(grid)
    cells = sorted([(grid[i][j], i, j) for i in range(n) for j in range(n)])
    parent = list(range(n * n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    active = [[False] * n for _ in range(n)]
    for h, i, j in cells:
        active[i][j] = True
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and active[ni][nj]:
                parent[find(i * n + j)] = find(ni * n + nj)
        if find(0) == find(n * n - 1):
            return h
    return grid[n - 1][n - 1]
