def solve(board: list[list[str]]) -> None:
    if not board:
        return
    m, n = len(board), len(board[0])

    def _dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = '#'
        _dfs(i + 1, j); _dfs(i - 1, j); _dfs(i, j + 1); _dfs(i, j - 1)

    for i in range(m):
        _dfs(i, 0); _dfs(i, n - 1)
    for j in range(n):
        _dfs(0, j); _dfs(m - 1, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'
