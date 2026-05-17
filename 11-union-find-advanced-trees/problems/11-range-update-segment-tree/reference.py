class RangeUpdateSum:
    def __init__(self, data: list[int]) -> None:
        self._n = len(data)
        self._t = [0] * (4 * max(1, self._n))
        self._lz = [0] * (4 * max(1, self._n))
        if self._n:
            self._build(1, 0, self._n - 1, data)

    def _build(self, node, lo, hi, data):
        if lo == hi:
            self._t[node] = data[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, data)
        self._build(2 * node + 1, mid + 1, hi, data)
        self._t[node] = self._t[2 * node] + self._t[2 * node + 1]

    def _push(self, node, lo, hi):
        if self._lz[node]:
            mid = (lo + hi) // 2
            for child, length in ((2 * node, mid - lo + 1), (2 * node + 1, hi - mid)):
                self._t[child] += self._lz[node] * length
                self._lz[child] += self._lz[node]
            self._lz[node] = 0

    def range_add(self, l, r, delta):
        self._update(1, 0, self._n - 1, l, r, delta)

    def _update(self, node, lo, hi, l, r, delta):
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r:
            self._t[node] += delta * (hi - lo + 1)
            self._lz[node] += delta
            return
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        self._update(2 * node, lo, mid, l, r, delta)
        self._update(2 * node + 1, mid + 1, hi, l, r, delta)
        self._t[node] = self._t[2 * node] + self._t[2 * node + 1]

    def range_sum(self, l, r):
        return self._q(1, 0, self._n - 1, l, r)

    def _q(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self._t[node]
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        return self._q(2 * node, lo, mid, l, r) + self._q(2 * node + 1, mid + 1, hi, l, r)
