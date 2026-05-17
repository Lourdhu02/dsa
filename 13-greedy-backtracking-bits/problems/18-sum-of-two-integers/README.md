# 18. Sum of two integers without + or -  `[medium]`

Compute the sum of two integers `a + b` without using `+` or `-`.

## Function signature

```python
def get_sum(a: int, b: int) -> int: ...
```

## Examples

| a | b | result |
|---|---|---|
| 1 | 2 | 3 |
| -1 | 1 | 0 |
| -2 | 3 | 1 |



## Hint

<details>
<summary>Hint</summary>

Carry-add via bitwise: `sum_no_carry = a ^ b`, `carry = (a & b) << 1`. Loop until carry == 0. Mask to 32 bits and reinterpret negatives because Python ints are unbounded.
</details>
