# 08. Longest consecutive sequence  `[medium]`

Given an unsorted integer array, return the length of the longest sequence of consecutive integers. Run in `Θ(n)`.

## Function signature

```python
def longest_consecutive(nums: list[int]) -> int: ...
```

## Examples

| nums | answer |
|---|---|
| `[100, 4, 200, 1, 3, 2]` | 4 (`[1, 2, 3, 4]`) |
| `[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]` | 9 |
| `[]` | 0 |



## Hint

<details>
<summary>Hint</summary>

Put all numbers in a set. For each `x` only start counting when `x - 1` is NOT in the set (so each run is processed once). Walk `x, x+1, x+2, ...` while present. Total work Θ(n) because every element is visited as part of at most one run.
</details>
