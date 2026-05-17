# 11. Design HashSet  `[easy]`

Implement `MyHashSet` with `add`, `remove`, `contains` — without using a built-in hash set.

## Function signature

```python
class MyHashSet:
    def add(self, key: int) -> None: ...
    def remove(self, key: int) -> None: ...
    def contains(self, key: int) -> bool: ...
```

## Examples

```
s = MyHashSet()
s.add(1); s.add(2)
s.contains(1)    # True
s.contains(3)    # False
s.remove(2)
s.contains(2)    # False
```



## Hint

<details>
<summary>Hint</summary>

Same backbone as MyHashMap but each slot holds a key, no value. Chaining is the simplest path.
</details>
