# 10. Repeated substring pattern  `[easy]`

Return True if `s` can be constructed by concatenating multiple copies of a non-empty proper substring.

## Function signature

```python
def repeated_substring_pattern(s: str) -> bool: ...
```

## Examples

| s | result |
|---|---|
| `"abab"` | True |
| `"aba"` | False |
| `"abcabcabcabc"` | True |



## Hint

<details>
<summary>Hint</summary>

Trick: `(s + s)[1:-1]` contains `s` iff `s` is repeated.
</details>
