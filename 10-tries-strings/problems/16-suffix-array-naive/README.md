# 16. Suffix array (naive build)  `[medium]`

Given a string `s`, return its suffix array — the indices `[i_0, i_1, ...]` such that `s[i_0:], s[i_1:], ...` is lexicographically sorted. Naive `Θ(n^2 log n)` is fine for the test sizes.

## Function signature

```python
def suffix_array(s: str) -> list[int]: ...
```

## Examples

| s | result |
|---|---|
| `"banana"` | `[5, 3, 1, 0, 4, 2]` |
| `"abc"` | `[0, 1, 2]` |



## Hint

<details>
<summary>Hint</summary>

Just `sorted(range(len(s)), key=lambda i: s[i:])`. Real-world implementations use SA-IS or DC3 in `Θ(n)`; we don't here.
</details>
