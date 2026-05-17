# 01. Implement DSU (Union-Find)  `[easy]`

Implement DSU on `n` elements with `find(x)`, `union(x, y) -> bool` (returns True if a merge happened), `connected(x, y) -> bool`, and `count` (number of components).

## Function signature

```python
class DSU:
    def __init__(self, n: int) -> None: ...
    def find(self, x: int) -> int: ...
    def union(self, x: int, y: int) -> bool: ...
    def connected(self, x: int, y: int) -> bool: ...
    count: int
```

## Examples

```
d = DSU(5)
d.union(0, 1)        # True
d.union(0, 1)        # False
d.connected(0, 1)    # True
d.connected(0, 2)    # False
d.count              # 4
```



## Hint

<details>
<summary>Hint</summary>

Path compression in find; union by rank in union.
</details>
