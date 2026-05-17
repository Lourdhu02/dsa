# 16. Redundant connection  `[medium]`

An undirected graph started as a tree (n nodes, n-1 edges) then had ONE extra edge added. The edge list is in input order. Return the last redundant edge.

## Function signature

```python
def find_redundant(edges: list[list[int]]) -> list[int]: ...
```

## Examples

| edges | result |
|---|---|
| `[[1, 2], [1, 3], [2, 3]]` | `[2, 3]` |
| `[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]` | `[1, 4]` |



## Hint

<details>
<summary>Hint</summary>

Union-find. Walk edges; the first that joins two nodes already in the same component is the redundant one.
</details>
