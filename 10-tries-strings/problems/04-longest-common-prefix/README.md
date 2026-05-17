# 04. Longest common prefix  `[easy]`

Return the longest common prefix among an array of strings; `""` if none.

## Function signature

```python
def longest_common_prefix(strs: list[str]) -> str: ...
```

## Examples

| strs | result |
|---|---|
| `["flower","flow","flight"]` | `"fl"` |
| `["dog","racecar","car"]` | `""` |



## Hint

<details>
<summary>Hint</summary>

Compare characters of all strings at each position until mismatch.
</details>
