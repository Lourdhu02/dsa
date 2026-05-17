# 14. Three sum  `[medium]`

Given an integer array `nums`, return **all unique triplets** `[a, b, c]` such that `a + b + c == 0`. The order of triplets in the output doesn't matter, but each triplet's elements should be non-decreasing.

Sort first, then for each `i`, two-pointer the rest of the array for pairs summing to `-nums[i]`. Sort + Θ(n²) two-pointer = **Θ(n²) total**.

## Function signature

```python
def three_sum(nums: list[int]) -> list[list[int]]: ...
```

## Examples

| nums | answer |
|---|---|
| `[-1, 0, 1, 2, -1, -4]` | `[[-1, -1, 2], [-1, 0, 1]]` |
| `[0, 1, 1]` | `[]` |
| `[0, 0, 0]` | `[[0, 0, 0]]` |

## Hint

<details>
<summary>Hint</summary>

1. Sort. 2. For each `i`, run two-pointer `(l = i+1, r = n-1)` over the rest. 3. Skip duplicates by advancing past equal neighbors at each level — both the outer `i` and the inner `l`/`r`.
</details>
