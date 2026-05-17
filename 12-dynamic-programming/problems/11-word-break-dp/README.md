# 11. Word break (DP)  `[medium]`

Same as module 10 #12 — included again to drill the DP perspective.

## Function signature

```python
def word_break(s: str, word_dict: list[str]) -> bool: ...
```

## Examples

| s | word_dict | result |
|---|---|---|
| `"leetcode"` | `["leet","code"]` | True |



## Hint

<details>
<summary>Hint</summary>

`dp[i]` True iff `s[:i]` is segmentable.
</details>
