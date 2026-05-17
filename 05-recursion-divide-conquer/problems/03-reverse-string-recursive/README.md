# 03. Reverse string (recursive)  `[easy]`

Reverse a list of characters in place using recursion. No explicit loops; no slicing tricks.

## Function signature

```python
def reverse_string(s: list[str]) -> None: ...
```

## Examples

| input | result |
|---|---|
| `["h","e","l","l","o"]` | `["o","l","l","e","h"]` |



## Hint

<details>
<summary>Hint</summary>

Helper `(l, r)` swaps and recurses `(l+1, r-1)` until `l >= r`.
</details>
