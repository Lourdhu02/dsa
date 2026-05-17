# 12. Isomorphic strings  `[easy]`

Two strings `s` and `t` are isomorphic if characters in `s` can be replaced consistently to obtain `t`. Each character must map to exactly one character, and no two characters may map to the same character.

## Function signature

```python
def is_isomorphic(s: str, t: str) -> bool: ...
```

## Examples

| s | t | result |
|---|---|---|
| `"egg"` | `"add"` | True |
| `"foo"` | `"bar"` | False |
| `"paper"` | `"title"` | True |



## Hint

<details>
<summary>Hint</summary>

Maintain two maps: `s -> t` and `t -> s`. Walk both strings in lockstep, checking that any existing mapping agrees.
</details>
