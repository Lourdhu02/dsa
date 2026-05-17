# 02. Number of provinces (DSU)  `[medium]`

Given an `n x n` matrix `is_connected[i][j] = 1` iff city `i` and `j` are directly connected, return the number of provinces (connected components).

## Function signature

```python
def find_circle_num(is_connected: list[list[int]]) -> int: ...
```

## Examples

| matrix | provinces |
|---|---|
| `[[1,1,0],[1,1,0],[0,0,1]]` | 2 |
| `[[1,0,0],[0,1,0],[0,0,1]]` | 3 |



## Hint

<details>
<summary>Hint</summary>

Walk upper triangle; union i, j on every 1.
</details>
