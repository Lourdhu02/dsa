class DynamicArray:
    """Dynamic array with explicit copy-count instrumentation.

    Per-op cost (CLRS § 17.4):
        push:         worst Θ(n), amortized Θ(1).
        __len__:      Θ(1).
        __getitem__:  Θ(1).
    Space: Θ(capacity), with capacity <= 2 * len at all times.
    """

    def __init__(self, initial_capacity: int = 1) -> None:
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be >= 1")
        self._buf: list[int | None] = [None] * initial_capacity
        self._n = 0
        self.copies = 0

    @property
    def capacity(self) -> int:
        return len(self._buf)

    def push(self, x: int) -> None:
        if self._n == self.capacity:
            new_cap = self.capacity * 2
            new_buf: list[int | None] = [None] * new_cap
            for i in range(self._n):
                new_buf[i] = self._buf[i]
                self.copies += 1
            self._buf = new_buf
        self._buf[self._n] = x
        self._n += 1

    def __len__(self) -> int:
        return self._n

    def __getitem__(self, i: int) -> int:
        if not 0 <= i < self._n:
            raise IndexError(i)
        # mypy/pyright happy: we never read None slots.
        return self._buf[i]  # type: ignore[return-value]
