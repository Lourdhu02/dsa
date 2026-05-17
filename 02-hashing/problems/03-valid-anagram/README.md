# 03. Valid anagram  `[easy]`

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`. Both strings consist of lowercase English letters.

## Function signature

```python
def is_anagram(s: str, t: str) -> bool: ...
```

## Examples

| s | t | result |
|---|---|---|
| `"anagram"` | `"nagaram"` | True |
| `"rat"` | `"car"` | False |
| `""` | `""` | True |



## Hint

<details>
<summary>Hint</summary>

Compare character counts. Either build two `Counter`s and compare, or sort both strings and compare.
</details>
