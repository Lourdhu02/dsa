# 01. Reverse string in place  `[easy]`

Reverse a list of single-character strings in place (modify the argument; return nothing). `O(1)` extra space.

## Function signature

```python
def reverse_string(s: list[str]) -> None: ...
```

## Examples

| input | result |
|---|---|
| `["h","e","l","l","o"]` | `["o","l","l","e","h"]` |
| `["a"]` | `["a"]` |
| `[]` | `[]` |

## Hint

<details>
<summary>Hint</summary>

Two pointers: swap `s[l]` and `s[r]`, then `l+=1; r-=1` until they meet.
</details>
