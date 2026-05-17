# 03. Min cost climbing stairs  `[easy]`

`cost[i]` is the cost to step on stair i. Once paid, you can step 1 or 2 stairs further. You can start at index 0 or 1. Return the min cost to reach past the last stair.

## Function signature

```python
def min_cost_climbing_stairs(cost: list[int]) -> int: ...
```

## Examples

| cost | result |
|---|---|
| `[10, 15, 20]` | 15 |
| `[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]` | 6 |



## Hint

<details>
<summary>Hint</summary>

`dp[i] = cost[i] + min(dp[i-1], dp[i-2])`. Final answer is `min(dp[n-1], dp[n-2])`.
</details>
