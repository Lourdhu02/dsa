# 08. Range sum query (segment tree)  `[medium]`

Implement `NumArray` with `update(i, val)` and `sum_range(l, r)` (inclusive), each `Θ(log n)`.

## Function signature

```python
class NumArray:
    def __init__(self, nums: list[int]) -> None: ...
    def update(self, i: int, val: int) -> None: ...
    def sum_range(self, l: int, r: int) -> int: ...
```

## Examples

```
na = NumArray([1, 3, 5])
na.sum_range(0, 2)   # 9
na.update(1, 2)
na.sum_range(0, 2)   # 8
```



## Hint

<details>
<summary>Hint</summary>

Segment tree.
</details>
