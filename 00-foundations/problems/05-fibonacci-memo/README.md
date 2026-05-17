# 05. Fibonacci (memoized)  `[easy]`

`fib(0) = 0`, `fib(1) = 1`, `fib(n) = fib(n-1) + fib(n-2)`. Implement a memoized recursive version.

The naive recursive version is `Θ(φ^n)` (exponential). Memoization caches each `fib(i)` and brings it to `Θ(n)` time and `Θ(n)` space. This is your first taste of dynamic programming.

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
| 30 | 832,040 |
| 100 | 354,224,848,179,261,915,075 |

## Constraints

- `0 <= n <= 500`

## Hint

<details>
<summary>Hint</summary>

Use `functools.lru_cache` (or a manual dict). The recursion tree has Θ(n) distinct subproblems; memoization makes each take Θ(1) amortized.
</details>

## Where this appears

`functools.lru_cache` is the production form of this pattern — every Python codebase that does memoization uses it. See https://docs.python.org/3/library/functools.html#functools.lru_cache.
