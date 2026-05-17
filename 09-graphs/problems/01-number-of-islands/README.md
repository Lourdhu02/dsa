# 01. Number of islands  `[medium]`

Given a 2D grid of `'1'` (land) and `'0'` (water), return the number of islands. An island is a maximal connected component of land cells, connected 4-directionally.

## Function signature

```python
def num_islands(grid: list[list[str]]) -> int: ...
```

## Examples

```
[['1','1','1','1','0'],
 ['1','1','0','1','0'],
 ['1','1','0','0','0'],
 ['0','0','0','0','0']]   -> 1

[['1','1','0','0','0'],
 ['1','1','0','0','0'],
 ['0','0','1','0','0'],
 ['0','0','0','1','1']]   -> 3
```



## Hint

<details>
<summary>Hint</summary>

Scan each cell; on '1' DFS/BFS to flood-fill, counting +1 per starting cell.
</details>
