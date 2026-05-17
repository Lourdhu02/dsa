# 04. First unique character  `[easy]`

Return the index of the first character in `s` that appears exactly once, or `-1` if no such character exists.

## Function signature

```python
def first_uniq_char(s: str) -> int: ...
```

## Examples

| s | result |
|---|---|
| `"leetcode"` | 0 |
| `"loveleetcode"` | 2 |
| `"aabb"` | -1 |



## Hint

<details>
<summary>Hint</summary>

Two passes: count characters, then scan the string and return the first index whose count is 1.
</details>
