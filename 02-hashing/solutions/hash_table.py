"""Two hand-rolled hash-table implementations.

This is the "show the data structure hand-rolled at least once" half of the
module — in real Python code you use ``dict`` directly.
"""

from __future__ import annotations

from typing import Iterator


class HashMapChaining:
    """Separate-chaining hash map.

    Time:
        - get/set/delete: Θ(1 + α) avg, Θ(n) worst.  Here α = n / m is the
          load factor.  We resize when α exceeds 0.75 to keep avg constant.
    Space: Θ(n + m) where m is the bucket count.

    Reference: CLRS 4th ed. § 11.2.
    """

    INITIAL_BUCKETS = 8
    LOAD_FACTOR_LIMIT = 0.75

    def __init__(self) -> None:
        self._buckets: list[list[tuple[object, object]]] = [[] for _ in range(self.INITIAL_BUCKETS)]
        self._n = 0

    def __len__(self) -> int:
        return self._n

    def __contains__(self, key: object) -> bool:
        for k, _ in self._bucket_for(key):
            if k == key:
                return True
        return False

    def get(self, key: object, default=None):
        for k, v in self._bucket_for(key):
            if k == key:
                return v
        return default

    def __getitem__(self, key: object):
        for k, v in self._bucket_for(key):
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key: object, value: object) -> None:
        bucket = self._bucket_for(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._n += 1
        if self._n / len(self._buckets) > self.LOAD_FACTOR_LIMIT:
            self._resize(len(self._buckets) * 2)

    def __delitem__(self, key: object) -> None:
        bucket = self._bucket_for(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._n -= 1
                return
        raise KeyError(key)

    def __iter__(self) -> Iterator:
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k

    def _bucket_for(self, key: object) -> list[tuple[object, object]]:
        return self._buckets[hash(key) % len(self._buckets)]

    def _resize(self, new_m: int) -> None:
        old = self._buckets
        self._buckets = [[] for _ in range(new_m)]
        self._n = 0
        for bucket in old:
            for k, v in bucket:
                self[k] = v


class HashSetOpenAddressing:
    """Linear-probing hash set with tombstones.

    Time:
        - add/contains/remove: Θ(1) avg (α < 0.5), Θ(n) worst.
    Space: Θ(m).

    Reference: CLRS 4th ed. § 11.4; CPython ``setobject.c``.
    """

    INITIAL_CAP = 8
    MAX_LOAD = 0.5

    _EMPTY = object()
    _TOMB = object()

    def __init__(self) -> None:
        self._slots: list[object] = [self._EMPTY] * self.INITIAL_CAP
        self._n = 0

    def __len__(self) -> int:
        return self._n

    def __contains__(self, key: object) -> bool:
        return self._probe(key)[1]

    def add(self, key: object) -> None:
        idx, found = self._probe(key)
        if not found:
            self._slots[idx] = key
            self._n += 1
            if self._n / len(self._slots) > self.MAX_LOAD:
                self._resize(len(self._slots) * 2)

    def remove(self, key: object) -> None:
        idx, found = self._probe(key)
        if not found:
            raise KeyError(key)
        self._slots[idx] = self._TOMB
        self._n -= 1

    def _probe(self, key: object) -> tuple[int, bool]:
        m = len(self._slots)
        h = hash(key) % m
        first_tomb = -1
        for step in range(m):
            i = (h + step) % m
            slot = self._slots[i]
            if slot is self._EMPTY:
                return (first_tomb if first_tomb >= 0 else i, False)
            if slot is self._TOMB:
                if first_tomb < 0:
                    first_tomb = i
                continue
            if slot == key:
                return i, True
        return (first_tomb if first_tomb >= 0 else 0, False)  # table full -- caller should resize

    def _resize(self, new_m: int) -> None:
        old = [s for s in self._slots if s is not self._EMPTY and s is not self._TOMB]
        self._slots = [self._EMPTY] * new_m
        self._n = 0
        for k in old:
            self.add(k)
