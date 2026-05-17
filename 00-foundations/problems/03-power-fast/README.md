# 03. Fast power  `[easy]`

Compute `a^n` for integer `a` and non-negative integer `n` using exponentiation by squaring (also called *binary exponentiation* or *Russian peasant exponentiation*) so the work is `Θ(log n)` multiplications.

The naive `Θ(n)` loop is a warm-up — implement it too so you can compare.

## Function signatures

```python
def power_linear(a: int, n: int) -> int: ...
def power_fast(a: int, n: int) -> int: ...
```

## Examples

| a | n | result |
|---|---|---|
| 2 | 10 | 1024 |
| 3 | 0 | 1 |
| 5 | 3 | 125 |
| -2 | 5 | -32 |

## Constraints

- `-100 <= a <= 100`
- `0 <= n <= 10^6` (linear version will get slow; fast version stays under 30 multiplications even at the top end).

## Hint

<details>
<summary>Hint</summary>

Use the identity `a^n = (a^(n/2))^2` when `n` is even, and `a^n = a * a^(n-1)` when `n` is odd. Iterative form: keep squaring `a` and consume bits of `n`.
</details>

## Where this appears in production

Modular exponentiation underlies RSA / Diffie-Hellman / signature verification. Numpy / PyTorch use a similar repeated-squaring approach for matrix powers in graph algorithms (e.g., counting walks of length `k`).
