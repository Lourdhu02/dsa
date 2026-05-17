"""Doubly-linked-list LRU cache.

Time per operation: Θ(1) amortized (hash-map insert/lookup + constant
pointer surgery).  Space: Θ(capacity).

Reference: this is the structure ``functools.lru_cache`` and many production
caches (Redis maxmemory-policy allkeys-lru, Caffeine in Java) use.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class _Node:
    key: object
    value: object
    prev: Optional["_Node"] = field(default=None, repr=False)
    next: Optional["_Node"] = field(default=None, repr=False)


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._cap = capacity
        self._map: dict[object, _Node] = {}
        # Sentinel head/tail simplify boundary cases — no None-check around list ends.
        self._head = _Node(key=None, value=None)
        self._tail = _Node(key=None, value=None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def __len__(self) -> int:
        return len(self._map)

    def get(self, key: object) -> object:
        node = self._map.get(key)
        if node is None:
            return -1
        self._move_to_front(node)
        return node.value

    def put(self, key: object, value: object) -> None:
        node = self._map.get(key)
        if node is not None:
            node.value = value
            self._move_to_front(node)
            return
        if len(self._map) == self._cap:
            self._evict_lru()
        node = _Node(key=key, value=value)
        self._map[key] = node
        self._insert_at_front(node)

    def _unlink(self, node: _Node) -> None:
        assert node.prev is not None and node.next is not None
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node: _Node) -> None:
        first = self._head.next
        assert first is not None
        node.prev = self._head
        node.next = first
        self._head.next = node
        first.prev = node

    def _move_to_front(self, node: _Node) -> None:
        self._unlink(node)
        self._insert_at_front(node)

    def _evict_lru(self) -> None:
        lru = self._tail.prev
        assert lru is not None and lru is not self._head
        self._unlink(lru)
        del self._map[lru.key]
