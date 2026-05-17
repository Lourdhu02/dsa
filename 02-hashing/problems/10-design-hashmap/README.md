# 10. Design HashMap  `[medium]`

Implement a `MyHashMap` class without using the built-in hash table. Support `put(key, value)`, `get(key) -> int` (return -1 if missing), `remove(key)`. Keys and values are non-negative integers.

## Function signature

```python
class MyHashMap:
    def put(self, key: int, value: int) -> None: ...
    def get(self, key: int) -> int: ...
    def remove(self, key: int) -> None: ...
```

## Examples

```
m = MyHashMap()
m.put(1, 1); m.put(2, 2)
m.get(1)            # 1
m.get(3)            # -1
m.put(2, 1)
m.get(2)            # 1
m.remove(2)
m.get(2)            # -1
```



## Hint

<details>
<summary>Hint</summary>

Separate chaining with a list of buckets. Bucket index = `hash(key) % m`. Resize when load factor exceeds ~0.75.
</details>
