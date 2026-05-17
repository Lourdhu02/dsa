def solve_sudoku(board: list[list[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties: list[tuple[int, int]] = []
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == '.':
                empties.append((r, c))
            else:
                rows[r].add(v); cols[c].add(v); boxes[(r // 3) * 3 + c // 3].add(v)

    def _bt(idx):
        if idx == len(empties):
            return True
        r, c = empties[idx]
        b = (r // 3) * 3 + c // 3
        for d in '123456789':
            if d in rows[r] or d in cols[c] or d in boxes[b]:
                continue
            board[r][c] = d
            rows[r].add(d); cols[c].add(d); boxes[b].add(d)
            if _bt(idx + 1):
                return True
            rows[r].remove(d); cols[c].remove(d); boxes[b].remove(d)
        board[r][c] = '.'
        return False

    _bt(0)
