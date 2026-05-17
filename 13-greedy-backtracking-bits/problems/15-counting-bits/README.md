# 15. Counting bits  `[easy]`

For `n >= 0`, return an array `out[i]` for `i in [0, n]` where `out[i]` is the number of set bits in `i`. Solve in `Θ(n)`.

## Function signature

```python
def count_bits(n: int) -> list[int]: ...
```

## Examples

| n | result |
|---|---|
| 5 | `[0, 1, 1, 2, 1, 2]` |
| 2 | `[0, 1, 1]` |



## Hint

<details>
<summary>Hint</summary>

`dp[i] = dp[i >> 1] + (i & 1)`.
</details>
