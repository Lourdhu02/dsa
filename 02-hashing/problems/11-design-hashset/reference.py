class MyHashSet:
    INIT_M = 16

    def __init__(self) -> None:
        self._buckets: list[list[int]] = [[] for _ in range(self.INIT_M)]
        self._n = 0

    def _bucket(self, key: int) -> list[int]:
        return self._buckets[key % len(self._buckets)]

    def add(self, key: int) -> None:
        b = self._bucket(key)
        if key not in b:
            b.append(key)
            self._n += 1
            if self._n / len(self._buckets) > 0.75:
                self._resize(len(self._buckets) * 2)

    def remove(self, key: int) -> None:
        b = self._bucket(key)
        if key in b:
            b.remove(key)
            self._n -= 1

    def contains(self, key: int) -> bool:
        return key in self._bucket(key)

    def _resize(self, new_m: int) -> None:
        items = [k for bucket in self._buckets for k in bucket]
        self._buckets = [[] for _ in range(new_m)]
        self._n = 0
        for k in items:
            self.add(k)
