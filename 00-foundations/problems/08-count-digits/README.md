# 08. Count digits  `[easy]`

Return the number of decimal digits in a non-negative integer `n`. `count_digits(0) = 1` (zero has one digit).

## Function signature

```python
def count_digits(n: int) -> int: ...
```

## Examples

| n | digits |
|---|---|
| 0 | 1 |
| 7 | 1 |
| 42 | 2 |
| 12345 | 5 |
| 10**100 | 101 |

## Hint

<details>
<summary>Hint</summary>

Divide by 10 in a loop and count, or compute `len(str(n))`. The loop form is `Θ(log10 n)` time, `Θ(1)` space.
</details>
