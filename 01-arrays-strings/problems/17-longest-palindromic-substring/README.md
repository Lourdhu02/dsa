# 17. Longest palindromic substring  `[medium]`

Given a string `s`, return the longest substring of `s` that is a palindrome.

The expand-around-center technique runs in `Θ(n²)` time, `Θ(1)` space. (Manacher's algorithm is `Θ(n)` — covered in module 10 as a follow-up.)

## Function signature

```python
def longest_palindrome(s: str) -> str: ...
```

## Examples

| s | one valid answer |
|---|---|
| `"babad"` | `"bab"` or `"aba"` |
| `"cbbd"` | `"bb"` |
| `"a"` | `"a"` |
| `"ac"` | `"a"` or `"c"` |

## Hint

<details>
<summary>Hint</summary>

Try each center `i` in `[0, n)`. Two cases: odd-length palindrome centered at `s[i]`, even-length palindrome centered between `s[i]` and `s[i+1]`. Expand while characters match.
</details>
