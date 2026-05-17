# 18. Distinct subsequences  `[hard]`

Given strings `s` and `t`, return the number of distinct subsequences of `s` that equal `t`.

## Function signature

```python
def num_distinct(s: str, t: str) -> int: ...
```

## Examples

| s | t | result |
|---|---|---|
| `"rabbbit"` | `"rabbit"` | 3 |
| `"babgbag"` | `"bag"` | 5 |



## Hint

<details>
<summary>Hint</summary>

`dp[i][j]` = number of subsequences of `s[:i]` equal to `t[:j]`. If `s[i-1] == t[j-1]`: `dp[i-1][j-1] + dp[i-1][j]`; else `dp[i-1][j]`.
</details>
