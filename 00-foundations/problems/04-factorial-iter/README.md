# 04. Factorial (iterative)  `[easy]`

Return `n!` for non-negative `n`. Use a loop, not recursion (recursive Python hits the default 1000-frame limit at `n = 1000`).

## Function signature

```python
def factorial(n: int) -> int: ...
```

## Examples

| n | n! |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 5 | 120 |
| 10 | 3,628,800 |

## Constraints

- `0 <= n <= 1000` (Python ints are arbitrary precision so no overflow concerns).

## Hint

<details>
<summary>Hint</summary>

Multiply 1 × 2 × ... × n. Watch the base case `0! = 1` (empty product).
</details>
