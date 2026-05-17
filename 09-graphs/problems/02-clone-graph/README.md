# 02. Clone undirected graph  `[medium]`

Given a reference to a node in a connected undirected graph, return a deep copy.

## Function signature

```python
class Node:
    val: int
    neighbors: list['Node']

def clone_graph(node: Node | None) -> Node | None: ...
```

## Examples

Graph `1 - 2, 1 - 4, 2 - 3, 3 - 4` cloned: same structure, all-new Node objects.



## Hint

<details>
<summary>Hint</summary>

BFS/DFS. Map original->copy. For each visited node, build its copy's neighbors list via the map.
</details>
