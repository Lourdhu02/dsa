# 06. Redundant connection (DSU)  `[medium]`

An undirected graph started as a tree (n nodes, n-1 edges) then had ONE extra edge added. Return the last redundant edge in input order.

## Function signature

```python
def find_redundant_connection(edges: list[list[int]]) -> list[int]: ...
```

## Examples

| edges | result |
|---|---|
| `[[1, 2], [1, 3], [2, 3]]` | `[2, 3]` |
| `[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]` | `[1, 4]` |



## Hint

<details>
<summary>Hint</summary>

DSU. First edge whose endpoints already share a root is redundant.
</details>
