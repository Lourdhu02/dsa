# 14. All paths from source to target  `[medium]`

Given a DAG `graph[i] = list of nodes that i can go to`, return all paths from node 0 to node n-1.

## Function signature

```python
def all_paths(graph: list[list[int]]) -> list[list[int]]: ...
```

## Examples

`[[1, 2], [3], [3], []]` → `[[0, 1, 3], [0, 2, 3]]`.



## Hint

<details>
<summary>Hint</summary>

DFS with current path; on reaching n-1, record a copy.
</details>
