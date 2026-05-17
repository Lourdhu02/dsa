# 02. Power (recursive fast)  `[easy]`

Recursive `Θ(log n)` exponentiation `a^n` for non-negative `n`. (Iterative version is in module 00; here state and use the divide-and-conquer recurrence.)

## Function signature

```python
def power(a: float, n: int) -> float: ...
```

## Examples

| a | n | result |
|---|---|---|
| 2.0 | 10 | 1024.0 |
| 2.0 | -2 | 0.25 |
| 0.0 | 0 | 1.0 |



## Hint

<details>
<summary>Hint</summary>

`a^n = (a^(n//2))^2` for even n; `a^n = a * a^(n-1)` for odd n. Handle negative n by taking 1 / power(a, -n).
</details>
