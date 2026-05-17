# 08. Minimum size subarray sum  `[medium]`

Given an array of **positive** integers and a positive target, return the **minimum length** of a contiguous subarray whose sum is `>= target`. Return 0 if none exists.

The positivity of the input is what makes the sliding window valid: extending the window monotonically increases the sum, so once it's `>= target`, every shrink that keeps it `>= target` gives a shorter valid window.

## Function signature

```python
def min_subarray_len(target: int, nums: list[int]) -> int: ...
```

## Examples

| target | nums | answer |
|---|---|---|
| 7 | `[2, 3, 1, 2, 4, 3]` | 2 (`[4, 3]`) |
| 4 | `[1, 4, 4]` | 1 |
| 11 | `[1, 1, 1, 1, 1, 1, 1, 1]` | 0 |

## Hint

<details>
<summary>Hint</summary>

Extend `r`, growing the window sum. While `sum >= target`, record `r - l + 1`, then shrink (`sum -= nums[l]; l += 1`).
</details>
