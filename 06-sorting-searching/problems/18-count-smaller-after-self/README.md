# 18. Count of smaller numbers after self  `[hard]`

Given an integer array `nums`, return an array `counts` where `counts[i]` is the number of elements to the right of `nums[i]` that are smaller. `Θ(n log n)`.

## Function signature

```python
def count_smaller(nums: list[int]) -> list[int]: ...
```

## Examples

| nums | counts |
|---|---|
| `[5, 2, 6, 1]` | `[2, 1, 1, 0]` |
| `[-1]` | `[0]` |
| `[-1, -1]` | `[0, 0]` |



## Hint

<details>
<summary>Hint</summary>

Modify merge sort: track original indices. During merge, when an element from the right half is placed before some elements still pending in the left half, increment the count for those left elements... actually simpler: count for left element when it is placed (i.e., right elements already taken == count to add).
</details>
