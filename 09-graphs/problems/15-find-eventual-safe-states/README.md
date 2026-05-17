# 15. Find eventual safe states  `[medium]`

A node is safe if every path starting from it eventually leads to a terminal (no outgoing edges) node. Return all safe nodes sorted.

## Function signature

```python
def eventual_safe_nodes(graph: list[list[int]]) -> list[int]: ...
```

## Examples

`[[1, 2], [2, 3], [5], [0], [5], [], []]` → `[2, 4, 5, 6]`.



## Hint

<details>
<summary>Hint</summary>

Reverse the graph; nodes reachable in the reverse from terminal-only nodes are safe. Or DFS with three colors (unvisited / on-stack / safe).
</details>
