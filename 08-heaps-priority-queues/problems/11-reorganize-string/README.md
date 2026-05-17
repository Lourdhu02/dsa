# 11. Reorganize string  `[medium]`

Rearrange the characters of `s` so that no two adjacent characters are equal. Return any valid result, or `""` if impossible.

## Function signature

```python
def reorganize_string(s: str) -> str: ...
```

## Examples

| s | possible result |
|---|---|
| `"aab"` | `"aba"` |
| `"aaab"` | `""` |



## Hint

<details>
<summary>Hint</summary>

Max-heap by frequency. Always emit the most-frequent letter that is NOT equal to the previous emitted letter.
</details>
