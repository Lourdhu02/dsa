# 15. Find K pairs with smallest sums  `[medium]`

Given two sorted arrays `nums1` and `nums2`, return the `k` pairs `(a, b)` with `a in nums1, b in nums2` having the smallest sums.

## Function signature

```python
def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]: ...
```

## Examples

| nums1 | nums2 | k | result |
|---|---|---|---|
| `[1, 7, 11]` | `[2, 4, 6]` | 3 | `[[1, 2], [1, 4], [1, 6]]` |



## Hint

<details>
<summary>Hint</summary>

Heap of (sum, i, j) seeded with j=0 for each i. Pop, push (i, j+1). Or seed with one row and expand.
</details>
