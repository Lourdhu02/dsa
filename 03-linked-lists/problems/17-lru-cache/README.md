# 17. LRU cache  `[medium]`

Implement an `LRUCache` with capacity `cap`. Support `get(key) -> int` (returns -1 if absent), `put(key, value)`. Both must run in average `Θ(1)`. When `put` exceeds capacity, evict the least-recently-used entry.

## Function signature

```python
class LRUCache:
    def __init__(self, capacity: int) -> None: ...
    def get(self, key: int) -> int: ...
    def put(self, key: int, value: int) -> None: ...
```

## Examples

```
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)         # 1
cache.put(3, 3)      # evicts 2
cache.get(2)         # -1
cache.put(4, 4)      # evicts 1
cache.get(1)         # -1
cache.get(3)         # 3
cache.get(4)         # 4
```

## Constraints

- `1 <= capacity <= 3000`


## Hint

<details>
<summary>Hint</summary>

Doubly-linked list + dict. Map key -> node; the list orders nodes by recency, head = most recent, tail = LRU. Sentinel head/tail simplify edge cases.
</details>
