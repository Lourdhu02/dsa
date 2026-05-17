# 02. Sum 1..n  `[easy]`

Return the sum `1 + 2 + ... + n` for non-negative `n`.

Implement **both** a `Θ(n)` loop version and a `Θ(1)` closed-form version. The point is to feel the difference between the two complexity classes for the same answer.

## Function signatures

```python
def sum_to_n_loop(n: int) -> int: ...
def sum_to_n_formula(n: int) -> int: ...
```

## Examples

| n | sum |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 4 | 10 |
| 100 | 5050 |

## Constraints

- `0 <= n <= 10^9` (formula must finish; loop will be too slow at the top end).

## Hint

<details>
<summary>Hint</summary>

The closed form is `n * (n + 1) // 2` (use integer division to avoid float drift).
</details>
