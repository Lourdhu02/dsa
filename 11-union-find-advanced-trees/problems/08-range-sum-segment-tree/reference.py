class NumArray:
    def __init__(self, nums: list[int]) -> None:
        self._n = len(nums)
        self._t = [0] * (4 * max(1, self._n))
        if self._n:
            self._build(1, 0, self._n - 1, nums)

    def _build(self, node, lo, hi, nums):
        if lo == hi:
            self._t[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        self._t[node] = self._t[2 * node] + self._t[2 * node + 1]

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    def _update(self, node, lo, hi, i, val):
        if lo == hi:
            self._t[node] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * node, lo, mid, i, val)
        else:
            self._update(2 * node + 1, mid + 1, hi, i, val)
        self._t[node] = self._t[2 * node] + self._t[2 * node + 1]

    def sum_range(self, l: int, r: int) -> int:
        return self._q(1, 0, self._n - 1, l, r)

    def _q(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self._t[node]
        mid = (lo + hi) // 2
        return self._q(2 * node, lo, mid, l, r) + self._q(2 * node + 1, mid + 1, hi, l, r)
