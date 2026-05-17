# 05. Permutations  `[medium]`

Return all permutations of a list of distinct integers. Order of permutations doesn't matter.

## Function signature

```python
def permute(nums: list[int]) -> list[list[int]]: ...
```

## Examples

| nums | result count |
|---|---|
| `[1, 2, 3]` | 6 |
| `[]` | 1 (the empty permutation) |



## Hint

<details>
<summary>Hint</summary>

Backtracking: at each step pick an unused element, recurse, undo.
</details>
