# 09. Pattern search with Rabin-Karp  `[medium]`

Implement Rabin-Karp pattern matching: return all starting indices of `pat` in `text`.

## Function signature

```python
def rabin_karp(text: str, pat: str) -> list[int]: ...
```

## Examples

| text | pat | result |
|---|---|---|
| `"abracadabra"` | `"abra"` | `[0, 7]` |



## Hint

<details>
<summary>Hint</summary>

Polynomial rolling hash mod a large prime; verify each hash hit with character compare to defeat collisions.
</details>
