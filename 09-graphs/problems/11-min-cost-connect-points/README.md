# 11. Min cost to connect all points (Prim MST)  `[medium]`

Given `points = [[x_i, y_i]]`, return the minimum cost to connect all points using Manhattan distance edges between every pair. (Equivalent to MST of the complete graph.)

## Function signature

```python
def min_cost_connect(points: list[list[int]]) -> int: ...
```

## Examples

| points | result |
|---|---|
| `[[0,0],[2,2],[3,10],[5,2],[7,0]]` | 20 |
| `[[3,12],[-2,5],[-4,1]]` | 18 |



## Hint

<details>
<summary>Hint</summary>

Prim's algorithm starting from any node, using a min-heap keyed on edge weight.
</details>
