def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    END = "$"
    root: dict = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node[END] = w

    found: list[str] = []
    m, n = len(board), len(board[0]) if board else 0

    def _dfs(i, j, node):
        ch = board[i][j]
        nxt = node.get(ch)
        if nxt is None:
            return
        word = nxt.pop(END, None)
        if word is not None:
            found.append(word)
        board[i][j] = "#"
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                _dfs(ni, nj, nxt)
        board[i][j] = ch
        if not nxt:
            node.pop(ch, None)

    for i in range(m):
        for j in range(n):
            _dfs(i, j, root)
    return found
