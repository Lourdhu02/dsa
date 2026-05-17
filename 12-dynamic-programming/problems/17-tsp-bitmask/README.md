# 17. Travelling salesman (bitmask DP)  `[hard]`

Given an `n x n` distance matrix (n ≤ 15), return the cost of the shortest tour visiting each city exactly once starting and ending at city 0.

## Function signature

```python
def tsp(dist: list[list[int]]) -> int: ...
```

## Examples

```
dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
result = 80
```

## Constraints

- `1 <= n <= 15`


## Hint

<details>
<summary>Hint</summary>

`dp[mask][i]` = min cost ending at city i having visited exactly the cities in mask. Transition: `dp[mask | 1<<j][j] = dp[mask][i] + dist[i][j]`.
</details>
