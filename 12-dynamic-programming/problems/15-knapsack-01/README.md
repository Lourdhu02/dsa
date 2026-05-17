# 15. 0/1 knapsack  `[medium]`

Given `weights`, `values`, and `capacity`, return the max value subset of items (each item at most once) with total weight ≤ capacity.

## Function signature

```python
def knapsack(weights: list[int], values: list[int], capacity: int) -> int: ...
```

## Examples

| weights | values | capacity | result |
|---|---|---|---|
| `[2, 3, 4, 5]` | `[3, 4, 5, 6]` | 5 | 7 |
| `[1, 2, 3]` | `[6, 10, 12]` | 5 | 22 |



## Hint

<details>
<summary>Hint</summary>

1D DP: outer loop items, inner loop capacity DESCENDING.
</details>
