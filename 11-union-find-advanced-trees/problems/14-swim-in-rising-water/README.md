# 14. Swim in rising water  `[hard]`

On `n x n` grid `grid[i][j]` is height. At time `t`, water reaches height `t`. From `(0, 0)` you may move to a neighbour iff both cells have `height <= t`. Return the minimum `t` to reach `(n-1, n-1)`.

## Function signature

```python
def swim_in_water(grid: list[list[int]]) -> int: ...
```

## Examples

| grid | result |
|---|---|
| `[[0, 2], [1, 3]]` | 3 |
| `[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]` | 16 |



## Hint

<details>
<summary>Hint</summary>

Sort cells by height; activate cells in order, union to active neighbours; return current height when (0,0) and (n-1,n-1) connect.
</details>
