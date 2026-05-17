# 10. Palindrome number  `[easy]`

Return `True` if the digits of `n` read the same forward and backward, else `False`. Negative numbers are not palindromes (the `-` sign breaks symmetry).

Implement two ways: (a) build a reversed integer (no string conversion) and compare; (b) compare digits from outside in. The two-pointer variant is the canonical pattern that comes back in module 01.

## Function signature

```python
def is_palindrome_number(n: int) -> bool: ...
```

## Examples

| n | palindrome? |
|---|---|
| 121 | True |
| -121 | False |
| 10 | False |
| 0 | True |
| 1234321 | True |

## Hint

<details>
<summary>Hint</summary>

Either reverse the digits (see problem 09) and compare, or repeatedly compare the leading and trailing digits while peeling them off.
</details>
