# 17. Range min query (segment tree)  `[medium]`

Implement `NumArrayMin` with `update(i, val)` and `range_min(l, r)` (inclusive) in `Θ(log n)`.

## Function signature

```python
class NumArrayMin:
    def __init__(self, nums: list[int]) -> None: ...
    def update(self, i: int, val: int) -> None: ...
    def range_min(self, l: int, r: int) -> int: ...
```

## Examples

```
nm = NumArrayMin([5, 2, 6, 1, 4])
nm.range_min(0, 4)   # 1
nm.update(3, 100)
nm.range_min(0, 4)   # 2
```



## Hint

<details>
<summary>Hint</summary>

Same skeleton as range-sum but combine with `min` and use a sentinel ∞ for empty queries.
</details>
