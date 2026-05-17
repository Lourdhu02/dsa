# 11. Count set bits  `[easy]`

Return the number of `1` bits in the binary representation of a non-negative integer (the *Hamming weight* or *popcount*).

There are three classic implementations — implement at least two:

1. **Mask + shift** — `Θ(b)` where `b = bit-width`.
2. **Brian Kernighan's trick** — `Θ(k)` where `k = set bits`. Strictly faster when `k << b`.
3. **Lookup table** — `Θ(b / 8)` table lookups per integer.

## Function signature

```python
def popcount(n: int) -> int: ...
```

## Examples

| n (decimal) | binary | popcount |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 1 | 1 |
| 7 | 111 | 3 |
| 11 | 1011 | 3 |
| 2^31 - 1 | 31 ones | 31 |

## Hint

<details>
<summary>Hint</summary>

Brian Kernighan: `n & (n - 1)` clears the lowest set bit. Repeat until `n == 0`, counting iterations.
</details>

## Production note

Python 3.10+ has `int.bit_count()` (implemented in C). Use the stdlib in real code; this exercise is to internalize the trick.
