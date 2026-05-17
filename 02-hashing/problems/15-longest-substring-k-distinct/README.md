# 15. Longest substring with at most K distinct characters  `[medium]`

Given a string `s` and integer `k`, return the length of the longest substring that contains at most `k` distinct characters.

## Function signature

```python
def longest_at_most_k(s: str, k: int) -> int: ...
```

## Examples

| s | k | answer |
|---|---|---|
| `"eceba"` | 2 | 3 (`"ece"`) |
| `"aa"` | 1 | 2 |
| `"abcadcacacaca"` | 3 | 11 |



## Hint

<details>
<summary>Hint</summary>

Sliding window. Maintain a count map of characters in the window. While the window has more than k distinct chars, shrink from the left.
</details>
