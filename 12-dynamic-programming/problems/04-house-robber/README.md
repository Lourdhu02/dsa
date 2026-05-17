# 04. House robber  `[medium]`

You cannot rob two adjacent houses. Return the max amount you can rob from a row of houses.

## Function signature

```python
def rob(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[1, 2, 3, 1]` | 4 |
| `[2, 7, 9, 3, 1]` | 12 |



## Hint

<details>
<summary>Hint</summary>

`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. O(1) space rolling.
</details>
