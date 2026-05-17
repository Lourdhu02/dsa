# 12. Unique paths in grid  `[medium]`

Robot at top-left of an `m x n` grid moves right or down. Return number of unique paths to bottom-right.

## Function signature

```python
def unique_paths(m: int, n: int) -> int: ...
```

## Examples

| m | n | result |
|---|---|---|
| 3 | 7 | 28 |
| 3 | 2 | 3 |
| 1 | 1 | 1 |



## Hint

<details>
<summary>Hint</summary>

`dp[i][j] = dp[i-1][j] + dp[i][j-1]`, with first row and column = 1.
</details>
