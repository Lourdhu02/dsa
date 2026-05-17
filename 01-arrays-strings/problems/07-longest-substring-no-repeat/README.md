# 07. Longest substring without repeating characters  `[medium]`

Given a string `s`, return the length of the longest substring with all distinct characters.

This is the canonical **variable-size sliding window** drill.

## Function signature

```python
def length_of_longest_substring(s: str) -> int: ...
```

## Examples

| s | answer |
|---|---|
| `"abcabcbb"` | 3 (`"abc"`) |
| `"bbbbb"` | 1 (`"b"`) |
| `"pwwkew"` | 3 (`"wke"`) |
| `""` | 0 |

## Hint

<details>
<summary>Hint</summary>

Keep a set of characters currently in the window. Extend `r`; while `s[r]` is in the set, remove `s[l]` and advance `l`. Track the max window size.
</details>
