# 10. Count inversions  `[hard]`

Given an integer array, return the number of *inversions* — pairs `(i, j)` with `i < j` and `nums[i] > nums[j]`. Solve in `Θ(n log n)`.

## Function signature

```python
def count_inversions(nums: list[int]) -> int: ...
```

## Examples

| nums | inversions |
|---|---|
| `[1, 3, 5, 2, 4, 6]` | 3 |
| `[5, 4, 3, 2, 1]` | 10 |
| `[1, 2, 3]` | 0 |



## Hint

<details>
<summary>Hint</summary>

Modify merge-sort. When you take an element from the right half during the merge while the left half still has `r` elements, add `r` to the inversion count.
</details>
