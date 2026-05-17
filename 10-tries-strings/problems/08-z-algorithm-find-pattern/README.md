# 08. Pattern matching with Z-algorithm  `[medium]`

Implement Z-algorithm-based pattern search: return all starting indices of `pat` in `text`.

## Function signature

```python
def z_find(text: str, pat: str) -> list[int]: ...
```

## Examples

| text | pat | result |
|---|---|---|
| `"aaaaa"` | `"aa"` | `[0, 1, 2, 3]` |
| `"abracadabra"` | `"abra"` | `[0, 7]` |



## Hint

<details>
<summary>Hint</summary>

Compute Z over `pat + '$' + text`; positions where Z == len(pat) are matches (offset by len(pat)+1).
</details>
