# 14. Fraction to recurring decimal  `[medium]`

Given numerator and denominator, return the decimal expansion as a string. If the fractional part repeats, enclose the repeating part in parentheses.

## Function signature

```python
def fraction_to_decimal(numerator: int, denominator: int) -> str: ...
```

## Examples

| n | d | result |
|---|---|---|
| 1 | 2 | `"0.5"` |
| 2 | 1 | `"2"` |
| 4 | 333 | `"0.(012)"` |
| -1 | -2147483648 | `"0.0000000004656612873077392578125"` |



## Hint

<details>
<summary>Hint</summary>

Long division.  Track remainders in a `dict[remainder, position_in_output]`. When a remainder repeats you've found the cycle start; insert `(` there and `)` at the end.
</details>
