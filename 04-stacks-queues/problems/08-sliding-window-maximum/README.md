# 08. Sliding window maximum  `[hard]`

Given array `nums` and integer `k`, return the maximum of each contiguous subarray of length `k`. Solve in `Θ(n)`.

## Function signature

```python
def max_sliding_window(nums: list[int], k: int) -> list[int]: ...
```

## Examples

| nums | k | result |
|---|---|---|
| `[1,3,-1,-3,5,3,6,7]` | 3 | `[3,3,5,5,6,7]` |
| `[1]` | 1 | `[1]` |
| `[9,11]` | 2 | `[11]` |



## Hint

<details>
<summary>Hint</summary>

Monotonic deque of indices, strictly decreasing in value. On each step: pop back while smaller-or-equal to new value; append new index; pop front if out of window. Front is window max.
</details>
