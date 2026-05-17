# 13. Word pattern  `[easy]`

Given a `pattern` (string of letters) and `s` (string of space-separated words), return True if `s` follows the same pattern: each letter must correspond to exactly one word and vice-versa.

## Function signature

```python
def word_pattern(pattern: str, s: str) -> bool: ...
```

## Examples

| pattern | s | result |
|---|---|---|
| `"abba"` | `"dog cat cat dog"` | True |
| `"abba"` | `"dog cat cat fish"` | False |
| `"aaaa"` | `"dog dog dog dog"` | True |



## Hint

<details>
<summary>Hint</summary>

Same bijection logic as `isomorphic-strings`, but with words on one side instead of characters.
</details>
