def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]

    def _dfs(i, j, seen):
        seen[i][j] = True
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and not seen[ni][nj] and heights[ni][nj] >= heights[i][j]:
                _dfs(ni, nj, seen)

    for i in range(m):
        _dfs(i, 0, pacific); _dfs(i, n - 1, atlantic)
    for j in range(n):
        _dfs(0, j, pacific); _dfs(m - 1, j, atlantic)
    out: list[list[int]] = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                out.append([i, j])
    return out
