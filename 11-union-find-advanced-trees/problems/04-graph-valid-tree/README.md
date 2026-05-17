# 04. Graph valid tree  `[medium]`

Given `n` nodes and an `edges` list, return True if the edges form a valid tree (connected, no cycles).

## Function signature

```python
def valid_tree(n: int, edges: list[list[int]]) -> bool: ...
```

## Examples

| n | edges | result |
|---|---|---|
| 5 | `[[0, 1], [0, 2], [0, 3], [1, 4]]` | True |
| 5 | `[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]` | False |



## Hint

<details>
<summary>Hint</summary>

Tree iff `len(edges) == n - 1` AND no cycle (DSU detects cycles when union returns False).
</details>
