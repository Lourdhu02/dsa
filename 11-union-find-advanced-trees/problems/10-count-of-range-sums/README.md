# 10. Count of range sums  `[hard]`

Given an integer array, return the number of pairs `(i, j)` with `i <= j` such that `lower <= sum(nums[i..j]) <= upper`.

## Function signature

```python
def count_range_sum(nums: list[int], lower: int, upper: int) -> int: ...
```

## Examples

| nums | lower | upper | result |
|---|---|---|---|
| `[-2, 5, -1]` | -2 | 2 | 3 |
| `[0]` | 0 | 0 | 1 |



## Hint

<details>
<summary>Hint</summary>

Modify merge-sort over prefix sums P. For each i, count j > i with `lower <= P[j] - P[i] <= upper`. Use the sortedness of right half to count in Θ(log n) per i.
</details>
