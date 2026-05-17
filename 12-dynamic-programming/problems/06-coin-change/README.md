# 06. Coin change (min coins)  `[medium]`

Given coin denominations and an amount, return the fewest coins needed to make the amount, or -1 if impossible.

## Function signature

```python
def coin_change(coins: list[int], amount: int) -> int: ...
```

## Examples

| coins | amount | result |
|---|---|---|
| `[1, 2, 5]` | 11 | 3 |
| `[2]` | 3 | -1 |
| `[1]` | 0 | 0 |



## Hint

<details>
<summary>Hint</summary>

`dp[a] = min(dp[a - c] + 1)` over coins `c <= a`. Initialize dp[0] = 0, others ∞.
</details>
