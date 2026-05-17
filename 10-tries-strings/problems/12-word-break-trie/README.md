# 12. Word break (trie + DP)  `[medium]`

Given a string `s` and a dictionary `word_dict`, return True if `s` can be segmented into a space-separated sequence of dictionary words.

## Function signature

```python
def word_break(s: str, word_dict: list[str]) -> bool: ...
```

## Examples

| s | word_dict | result |
|---|---|---|
| `"leetcode"` | `["leet","code"]` | True |
| `"applepenapple"` | `["apple","pen"]` | True |
| `"catsandog"` | `["cats","dog","sand","and","cat"]` | False |



## Hint

<details>
<summary>Hint</summary>

DP: `dp[i]` = True if `s[:i]` is segmentable. Walk the suffix dictionary at each position via a trie or set.
</details>
