# 13. Unique paths II (with obstacles)  `[medium]`

Same as #12 but `grid[i][j] == 1` is an obstacle.

## Function signature

```python
def unique_paths_with_obstacles(grid: list[list[int]]) -> int: ...
```

## Examples

| grid | result |
|---|---|
| `[[0,0,0],[0,1,0],[0,0,0]]` | 2 |
| `[[0,1],[0,0]]` | 1 |



## Hint

<details>
<summary>Hint</summary>

If `grid[i][j] == 1`, set `dp[i][j] = 0`.
</details>
