# 06. Subsets (power set)  `[medium]`

Return all subsets of an input list of distinct integers (the power set). Each subset can appear in any order; the list of subsets can be in any order.

## Function signature

```python
def subsets(nums: list[int]) -> list[list[int]]: ...
```

## Examples

| nums | count |
|---|---|
| `[1, 2, 3]` | 8 |
| `[]` | 1 |



## Hint

<details>
<summary>Hint</summary>

For each element decide *include or skip*. Recursion tree has 2^n leaves, each a subset.
</details>
