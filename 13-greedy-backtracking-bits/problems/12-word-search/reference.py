def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def _dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False
        ch = board[i][j]
        board[i][j] = '#'
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if _dfs(i + di, j + dj, k + 1):
                board[i][j] = ch
                return True
        board[i][j] = ch
        return False

    for i in range(m):
        for j in range(n):
            if _dfs(i, j, 0):
                return True
    return False
