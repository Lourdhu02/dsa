class DSU:
    def __init__(self, n: int) -> None:
        self._p = list(range(n))
        self._r = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        root = x
        while self._p[root] != root:
            root = self._p[root]
        while self._p[x] != root:
            self._p[x], x = root, self._p[x]
        return root

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self._r[rx] < self._r[ry]:
            rx, ry = ry, rx
        self._p[ry] = rx
        if self._r[rx] == self._r[ry]:
            self._r[rx] += 1
        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
