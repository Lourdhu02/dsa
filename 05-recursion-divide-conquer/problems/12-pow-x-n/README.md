# 12. Pow(x, n)  `[medium]`

Compute `x^n` for float `x` and integer `n` in `Θ(log |n|)`.

## Function signature

```python
def my_pow(x: float, n: int) -> float: ...
```

## Examples

| x | n | result |
|---|---|---|
| 2.0 | 10 | 1024.0 |
| 2.1 | 3 | 9.261 |
| 2.0 | -2 | 0.25 |



## Hint

<details>
<summary>Hint</summary>

Recurse on n // 2, square, fix the parity. Negative n: take 1 / pow(x, -n).
</details>
