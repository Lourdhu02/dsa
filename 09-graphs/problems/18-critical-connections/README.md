# 18. Critical connections (bridges)  `[hard]`

An undirected graph has `n` nodes and a list of connections. Return all *critical* connections — edges whose removal disconnects the graph.

## Function signature

```python
def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]: ...
```

## Examples

`n=4, connections=[[0,1],[1,2],[2,0],[1,3]]` → `[[1, 3]]`.



## Hint

<details>
<summary>Hint</summary>

Tarjan's bridge-finding algorithm. DFS with discovery times and `low[u]` = smallest discovery reachable. Edge `(u, v)` is a bridge iff `low[v] > disc[u]`.
</details>
