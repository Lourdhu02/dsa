def combine(n: int, k: int) -> list[list[int]]:
    out: list[list[int]] = []
    path: list[int] = []

    def _bt(start):
        if len(path) == k:
            out.append(path[:])
            return
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            _bt(i + 1)
            path.pop()

    _bt(1)
    return out
