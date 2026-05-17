# 15. Longest consecutive sequence (DSU)  `[medium]`

Given an unsorted integer array, return the length of the longest run of consecutive integers. Solve with DSU. (Module 02 covered the hash-set version.)

## Function signature

```python
def longest_consecutive(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[100, 4, 200, 1, 3, 2]` | 4 |
| `[]` | 0 |



## Hint

<details>
<summary>Hint</summary>

Index-based DSU. For each value `v`, union with `v+1` if seen. Track component sizes.
</details>
