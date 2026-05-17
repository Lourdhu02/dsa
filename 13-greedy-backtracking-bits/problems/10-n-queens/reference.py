def solve_n_queens(n: int) -> list[list[str]]:
    out: list[list[str]] = []
    cols: set[int] = set()
    diag1: set[int] = set()
    diag2: set[int] = set()
    placement: list[int] = []

    def _bt(r):
        if r == n:
            board = []
            for col in placement:
                row = ["."] * n
                row[col] = "Q"
                board.append("".join(row))
            out.append(board)
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            cols.add(c); diag1.add(r - c); diag2.add(r + c); placement.append(c)
            _bt(r + 1)
            cols.remove(c); diag1.remove(r - c); diag2.remove(r + c); placement.pop()

    _bt(0)
    return out
