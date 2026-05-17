# 16. Trailing zeros of n!  `[medium]`

Return the number of trailing zeros in `n!`.

The naive way is to compute `n!` (huge) and count trailing zeros. The clever way uses Legendre's formula: the number of trailing zeros equals the multiplicity of 5 in `n!` (since multiplicity of 2 is always larger). That gives `floor(n/5) + floor(n/25) + floor(n/125) + ...`.

## Function signature

```python
def trailing_zeros(n: int) -> int: ...
```

## Examples

| n | n! | trailing zeros |
|---|---|---|
| 0 | 1 | 0 |
| 4 | 24 | 0 |
| 5 | 120 | 1 |
| 10 | 3,628,800 | 2 |
| 25 | ... | 6 |
| 100 | ... | 24 |

## Constraints

- `0 <= n <= 10^9`

## Hint

<details>
<summary>Hint</summary>

Loop dividing by 5 while > 0: `count += n // 5; n //= 5`. Time is `Θ(log_5 n)`.
</details>
