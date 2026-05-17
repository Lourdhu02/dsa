# 13. Is graph bipartite  `[medium]`

Given an undirected adjacency-list graph `graph[i] = neighbors of node i`, return True iff it's bipartite (2-colorable).

## Function signature

```python
def is_bipartite(graph: list[list[int]]) -> bool: ...
```

## Examples

| graph | result |
|---|---|
| `[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]` | False |
| `[[1, 3], [0, 2], [1, 3], [0, 2]]` | True |



## Hint

<details>
<summary>Hint</summary>

BFS coloring. Color each component with 2 colors; conflict → not bipartite.
</details>
