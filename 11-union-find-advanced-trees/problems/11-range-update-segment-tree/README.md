# 11. Range update, range sum (lazy propagation)  `[hard]`

Implement `RangeUpdateSum`: build from list, `range_add(l, r, delta)` adds `delta` to every element in [l, r], `range_sum(l, r)` returns the inclusive sum. Both Θ(log n).

## Function signature

```python
class RangeUpdateSum:
    def __init__(self, data: list[int]) -> None: ...
    def range_add(self, l: int, r: int, delta: int) -> None: ...
    def range_sum(self, l: int, r: int) -> int: ...
```

## Examples

```
ru = RangeUpdateSum([1, 1, 1, 1])
ru.range_add(0, 2, 5)
ru.range_sum(0, 3)   # (6+6+6+1) = 19
```



## Hint

<details>
<summary>Hint</summary>

Standard lazy seg tree. `lazy[node]` accumulates pending +delta to be pushed to children on the next descent.
</details>
