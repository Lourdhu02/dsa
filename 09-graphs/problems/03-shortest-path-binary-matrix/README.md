# 03. Shortest path in binary matrix  `[medium]`

In an `n x n` binary matrix, return the length of the shortest path from `(0, 0)` to `(n-1, n-1)` walking through 0-cells using 8-directional steps. Return -1 if no such path exists.

## Function signature

```python
def shortest_path(grid: list[list[int]]) -> int: ...
```

## Examples

| grid | result |
|---|---|
| `[[0, 1], [1, 0]]` | 2 |
| `[[0, 0, 0], [1, 1, 0], [1, 1, 0]]` | 4 |



## Hint

<details>
<summary>Hint</summary>

BFS over 8-neighbours. Track distance per cell.
</details>
