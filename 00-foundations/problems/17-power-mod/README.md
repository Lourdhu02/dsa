# 17. Modular exponentiation  `[medium]`

Compute `a^n mod m` for `a >= 0`, `n >= 0`, `m > 0` in `Θ(log n)` time.

This is the backbone of RSA encryption and signature verification. It also powers Rabin-Karp's rolling hash (module 10).

## Function signature

```python
def pow_mod(a: int, n: int, m: int) -> int: ...
```

## Examples

| a | n | m | result |
|---|---|---|---|
| 2 | 10 | 1000 | 24 |
| 5 | 0 | 7 | 1 |
| 3 | 200 | 13 | 9 |
| 7 | 1_000_000 | 19 | 1 |

## Constraints

- `0 <= a <= 10^18`
- `0 <= n <= 10^18`
- `1 <= m <= 10^18`

## Hint

<details>
<summary>Hint</summary>

Same shape as the fast-power problem; take `mod m` after every multiplication so intermediate values stay bounded.
</details>

## Production note

Python's built-in `pow(a, n, m)` is the right thing in real code — it's implemented in C and uses Montgomery / sliding-window optimizations. We reimplement here to understand the structure.
