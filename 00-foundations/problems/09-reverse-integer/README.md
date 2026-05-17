# 09. Reverse integer digits  `[easy]`

Reverse the decimal digits of an integer. Preserve the sign. Leading zeros after reversal are dropped.

## Function signature

```python
def reverse_integer(n: int) -> int: ...
```

## Examples

| n | result |
|---|---|
| 123 | 321 |
| -456 | -654 |
| 1200 | 21 |
| 0 | 0 |
| 1000000003 | 3000000001 |

## Constraints

- `-2^63 <= n < 2^63` (Python ints are arbitrary precision but tests stay within int64).

## Hint

<details>
<summary>Hint</summary>

Extract digits with `n % 10`, build the result by multiplying by 10 and adding. Track the sign separately.
</details>
