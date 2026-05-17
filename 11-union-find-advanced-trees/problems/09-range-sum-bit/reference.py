class NumArray:
    def __init__(self, nums: list[int]) -> None:
        self._n = len(nums)
        self._a = nums[:]
        self._t = [0] * (self._n + 1)
        for i, v in enumerate(nums, start=1):
            self._add(i, v)

    def _add(self, i, delta):
        while i <= self._n:
            self._t[i] += delta
            i += i & -i

    def _prefix(self, i):
        s = 0
        while i > 0:
            s += self._t[i]
            i -= i & -i
        return s

    def update(self, i: int, val: int) -> None:
        delta = val - self._a[i]
        self._a[i] = val
        self._add(i + 1, delta)

    def sum_range(self, l: int, r: int) -> int:
        return self._prefix(r + 1) - self._prefix(l)
