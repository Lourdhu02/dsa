# 16. MST cost (Kruskal + DSU)  `[medium]`

Given `n` nodes 0..n-1 and a list of weighted edges `[u, v, w]`, return the cost of the minimum spanning tree, or -1 if the graph is disconnected.

## Function signature

```python
def mst_cost(n: int, edges: list[list[int]]) -> int: ...
```

## Examples

| n | edges | result |
|---|---|---|
| 4 | `[[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 10]]` | 6 |



## Hint

<details>
<summary>Hint</summary>

Sort edges by weight; union; sum weights of accepted edges.
</details>
