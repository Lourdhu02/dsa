# 10. Edit distance (Levenshtein)  `[hard]`

Return the minimum number of single-character insertions, deletions, or substitutions to transform `s` into `t`.

## Function signature

```python
def min_distance(s: str, t: str) -> int: ...
```

## Examples

| s | t | result |
|---|---|---|
| `"horse"` | `"ros"` | 3 |
| `"intention"` | `"execution"` | 5 |



## Hint

<details>
<summary>Hint</summary>

Standard 2D DP. Space-optimize to one row.
</details>
