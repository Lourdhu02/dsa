# 05. Maximum sum of a subarray of size k  `[easy]`

Given an integer array `nums` and a positive integer `k`, return the maximum sum of any **contiguous** subarray of length exactly `k`.

This is the canonical **fixed-size sliding window** drill. Don't recompute the sum from scratch each step — slide.

## Function signature

```python
def max_sum_k(nums: list[int], k: int) -> int: ...
```

## Examples

| nums | k | answer |
|---|---|---|
| `[2, 1, 5, 1, 3, 2]` | 3 | 9 (subarray `[5, 1, 3]`) |
| `[5, 5, 5, 5]` | 2 | 10 |
| `[7]` | 1 | 7 |

## Constraints

- `1 <= k <= len(nums)`

## Hint

<details>
<summary>Hint</summary>

Initialize `window = sum(nums[:k])`. Slide: `window += nums[r] - nums[r - k]`. Track the running max.
</details>
