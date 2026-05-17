# 09. Subarray sum equals k  `[medium]`

Given an integer array `nums` (can include negatives) and an integer `k`, return the **number** of contiguous subarrays whose sum is exactly `k`.

Sliding window does **not** work here because the array can contain negatives — extending the window doesn't monotonically change the sum. Use the **prefix-sum + hash map** pattern: for each prefix sum `P[i]`, count how many earlier prefixes `P[j]` satisfy `P[i] - P[j] == k`, i.e. `P[j] == P[i] - k`.

## Function signature

```python
def subarray_sum(nums: list[int], k: int) -> int: ...
```

## Examples

| nums | k | answer |
|---|---|---|
| `[1, 1, 1]` | 2 | 2 |
| `[1, 2, 3]` | 3 | 2 |
| `[1, -1, 1, -1]` | 0 | 4 |

## Hint

<details>
<summary>Hint</summary>

Walk left to right, maintaining running prefix sum `cur`. For each `cur`, the number of subarrays ending here with sum `k` is `count[cur - k]`. Initialize `count = {0: 1}` so prefixes that themselves equal `k` are counted.
</details>

## Where this appears

A common subroutine when you need *any* "subarray with property X" count in `Θ(n)`: range XOR == k, range product == k (with logs), range mod-class. Same skeleton.
