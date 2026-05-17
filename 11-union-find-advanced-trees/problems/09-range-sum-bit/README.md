# 09. Range sum query (BIT)  `[medium]`

Same problem as #08 but implement with a Binary Indexed Tree.

## Function signature

```python
class NumArray:
    def __init__(self, nums: list[int]) -> None: ...
    def update(self, i: int, val: int) -> None: ...
    def sum_range(self, l: int, r: int) -> int: ...
```

## Examples

Same as the segment-tree version.



## Hint

<details>
<summary>Hint</summary>

BIT operates on prefix sums; convert update to a delta against the current value.
</details>
