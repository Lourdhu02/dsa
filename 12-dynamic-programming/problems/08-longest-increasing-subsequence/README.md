# 08. Longest increasing subsequence  `[medium]`

Return the length of the longest strictly increasing subsequence of `nums`. Solve in `Θ(n log n)`.

## Function signature

```python
def length_of_lis(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[10, 9, 2, 5, 3, 7, 101, 18]` | 4 |
| `[0, 1, 0, 3, 2, 3]` | 4 |
| `[7, 7, 7, 7]` | 1 |



## Hint

<details>
<summary>Hint</summary>

Patience sorting: maintain `tails` array; for each x, replace `tails[bisect_left(tails, x)]` (or append).
</details>
