# 07. Find min in rotated sorted array  `[medium]`

Sorted array of distinct ints was rotated at an unknown pivot. Return the minimum element. `Θ(log n)`.

## Function signature

```python
def find_min(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[3, 4, 5, 1, 2]` | 1 |
| `[4, 5, 6, 7, 0, 1, 2]` | 0 |
| `[11, 13, 15, 17]` | 11 |



## Hint

<details>
<summary>Hint</summary>

Compare `nums[mid]` to `nums[hi]`. If greater, min is in `[mid+1, hi]`; else in `[lo, mid]`.
</details>
