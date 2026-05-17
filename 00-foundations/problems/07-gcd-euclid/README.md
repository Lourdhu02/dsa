# 07. GCD via Euclid's algorithm  `[easy]`

Compute the greatest common divisor of two non-negative integers using

```
gcd(a, b) = gcd(b, a mod b),   gcd(a, 0) = a
```

This is one of the oldest known algorithms (Euclid, ~300 BCE) and one of the cleanest examples of `Θ(log min(a, b))` — the modulus shrinks fast.

## Function signature

```python
def gcd(a: int, b: int) -> int: ...
```

## Examples

| a | b | gcd |
|---|---|---|
| 48 | 18 | 6 |
| 0 | 7 | 7 |
| 7 | 0 | 7 |
| 1071 | 462 | 21 |
| 17 | 13 | 1 |

## Constraints

- `0 <= a, b <= 10^18`

## Hint

<details>
<summary>Hint</summary>

Iterate: `a, b = b, a % b` until `b == 0`. Return `a`. The worst case (Fibonacci pair) gives `Θ(log φ b)` iterations — Lamé's theorem.
</details>
