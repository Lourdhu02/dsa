# 13. Maximum subarray (Kadane)  `[medium]`

Given an integer array `nums` (may contain negatives), return the largest sum of any **contiguous, non-empty** subarray.

## Function signature

```python
def max_subarray(nums: list[int]) -> int: ...
```

## Examples

| nums | answer |
|---|---|
| `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` | 6 |
| `[1]` | 1 |
| `[5, 4, -1, 7, 8]` | 23 |
| `[-3, -2, -1]` | -1 |

## Hint

<details>
<summary>Hint</summary>

`ending_here = max(x, ending_here + x); best = max(best, ending_here)`. See `solutions/kadane.py`.
</details>

## Follow-up

There's also a divide-and-conquer formulation that runs in `Θ(n log n)` — covered in module 05.
