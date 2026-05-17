# 15. Integer square root  `[medium]`

Return the largest non-negative integer `r` such that `r * r <= n`. Use **binary search** — no floats, no `math.sqrt`.

## Function signature

```python
def isqrt(n: int) -> int: ...
```

## Examples

| n | isqrt |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 4 | 2 |
| 8 | 2 |
| 16 | 4 |
| 99 | 9 |
| 10**18 | 1000000000 |

## Constraints

- `0 <= n <= 10^18`

## Hint

<details>
<summary>Hint</summary>

Binary search `r` in `[0, n]`. Invariant: every value in `[lo, hi]` is still a candidate. Move `lo = mid + 1` when `mid*mid <= n`, else `hi = mid - 1`. Return `lo - 1` (or `hi` — pick one and prove correctness).
</details>

## Production note

`math.isqrt(n)` (Python 3.8+) does exactly this in C. We implement it here to internalize the binary-search invariant.
