class MyHashMap:
    """Separate chaining.  Amortized Θ(1) avg per op."""

    INIT_M = 16
    LIMIT = 0.75

    def __init__(self) -> None:
        self._buckets: list[list[tuple[int, int]]] = [[] for _ in range(self.INIT_M)]
        self._n = 0

    def _bucket(self, key: int) -> list[tuple[int, int]]:
        return self._buckets[key % len(self._buckets)]

    def put(self, key: int, value: int) -> None:
        b = self._bucket(key)
        for i, (k, _) in enumerate(b):
            if k == key:
                b[i] = (key, value)
                return
        b.append((key, value))
        self._n += 1
        if self._n / len(self._buckets) > self.LIMIT:
            self._resize(len(self._buckets) * 2)

    def get(self, key: int) -> int:
        for k, v in self._bucket(key):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        b = self._bucket(key)
        for i, (k, _) in enumerate(b):
            if k == key:
                del b[i]
                self._n -= 1
                return

    def _resize(self, new_m: int) -> None:
        old_items = [(k, v) for bucket in self._buckets for (k, v) in bucket]
        self._buckets = [[] for _ in range(new_m)]
        self._n = 0
        for k, v in old_items:
            self.put(k, v)
