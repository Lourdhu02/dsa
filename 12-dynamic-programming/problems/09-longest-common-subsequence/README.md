# 09. Longest common subsequence  `[medium]`

Return the length of the longest common subsequence of two strings.

## Function signature

```python
def lcs(s: str, t: str) -> int: ...
```

## Examples

| s | t | result |
|---|---|---|
| `"abcde"` | `"ace"` | 3 |
| `"abc"` | `"abc"` | 3 |
| `"abc"` | `"def"` | 0 |



## Hint

<details>
<summary>Hint</summary>

`dp[i][j] = dp[i-1][j-1] + 1` if `s[i-1] == t[j-1]` else `max(dp[i-1][j], dp[i][j-1])`.
</details>
