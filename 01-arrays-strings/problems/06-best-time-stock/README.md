# 06. Best time to buy and sell stock  `[easy]`

`prices[i]` is the price of a stock on day `i`. Choose ONE day to buy and ONE later day to sell to maximize profit. Return the max profit, or 0 if no profitable trade is possible.

## Function signature

```python
def max_profit(prices: list[int]) -> int: ...
```

## Examples

| prices | answer |
|---|---|
| `[7, 1, 5, 3, 6, 4]` | 5 (buy at 1, sell at 6) |
| `[7, 6, 4, 3, 1]` | 0 |
| `[1]` | 0 |
| `[2, 4, 1]` | 2 |

## Hint

<details>
<summary>Hint</summary>

Track the running minimum price seen so far. On each day, update the best profit if `price - min_so_far` improves it.
</details>
