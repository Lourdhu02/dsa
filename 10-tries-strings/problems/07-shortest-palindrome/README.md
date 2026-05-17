# 07. Shortest palindrome  `[hard]`

Return the shortest palindrome you can form by adding characters to the front of `s`.

## Function signature

```python
def shortest_palindrome(s: str) -> str: ...
```

## Examples

| s | result |
|---|---|
| `"aacecaaa"` | `"aaacecaaa"` |
| `"abcd"` | `"dcbabcd"` |



## Hint

<details>
<summary>Hint</summary>

Find the longest palindromic prefix. Use KMP failure on `s + '#' + reverse(s)`.
</details>
