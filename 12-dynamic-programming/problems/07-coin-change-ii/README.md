# 07. Coin change II (count combinations)  `[medium]`

Return the number of distinct combinations of coins that sum to `amount`.

## Function signature

```python
def coin_change_count(amount: int, coins: list[int]) -> int: ...
```

## Examples

| amount | coins | result |
|---|---|---|
| 5 | `[1, 2, 5]` | 4 |
| 3 | `[2]` | 0 |
| 10 | `[10]` | 1 |



## Hint

<details>
<summary>Hint</summary>

`dp[a] += dp[a - c]`. Outer loop over coins (not amounts) to avoid double-counting orderings.
</details>
