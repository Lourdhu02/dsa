# 10. Pacific Atlantic water flow  `[medium]`

Given a 2D matrix of heights, return all cells from which water can flow to both the Pacific (top/left edges) and Atlantic (bottom/right edges). Water flows to a neighbor with equal or lower height.

## Function signature

```python
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]: ...
```

## Examples

```
[[1, 2, 2, 3, 5],
 [3, 2, 3, 4, 4],
 [2, 4, 5, 3, 1],
 [6, 7, 1, 4, 5],
 [5, 1, 1, 2, 4]]
result: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```



## Hint

<details>
<summary>Hint</summary>

Reverse the flow: BFS/DFS from each ocean (upstream — only step to equal-or-higher cells). Intersection of reachable sets is the answer.
</details>
