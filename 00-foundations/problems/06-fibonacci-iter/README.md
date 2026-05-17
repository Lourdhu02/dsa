# 06. Fibonacci (iterative, O(1) space)  `[easy]`

Same answers as problem 05 but use a loop that keeps only the last two values. This drops space from `Θ(n)` (recursion + cache) to `Θ(1)`.

## Function signature

```python
def fib(n: int) -> int: ...
```

## Examples

| n | fib(n) |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 10 | 55 |
| 100 | 354,224,848,179,261,915,075 |

## Constraints

- `0 <= n <= 10000` (Python bignum arithmetic is what bounds you in practice).

## Hint

<details>
<summary>Hint</summary>

Carry two variables `(prev, curr) = (0, 1)`. On each step `(prev, curr) = (curr, prev + curr)`. Python's tuple-unpacking does the swap atomically — no temporary needed.
</details>

## Big-O comparison

| Version | Time | Space | Notes |
|---|---|---|---|
| Naive recursive | Θ(φ^n) | Θ(n) stack | Avoid for n > 30. |
| Memoized (problem 05) | Θ(n) | Θ(n) | Cache + stack. |
| Iterative (this) | Θ(n) | Θ(1) | Best default. |
| Matrix exponentiation | Θ(log n) | Θ(1) | Worth knowing; covered in module 05. |
