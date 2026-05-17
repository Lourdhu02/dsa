# 05. Find peak element  `[medium]`

A peak is strictly greater than its neighbors. Find any peak index in `Θ(log n)`. Assume `nums[-1] = nums[n] = -inf`.

## Function signature

```python
def find_peak(nums: list[int]) -> int: ...
```

## Examples

| nums | possible result |
|---|---|
| `[1, 2, 3, 1]` | 2 |
| `[1, 2, 1, 3, 5, 6, 4]` | 1 or 5 |



## Hint

<details>
<summary>Hint</summary>

Compare `nums[mid]` to `nums[mid+1]`. If smaller, peak is in `[mid+1, hi]`; else in `[lo, mid]`. The slope must change since the boundaries are -inf.
</details>
