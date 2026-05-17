# 01. Factorial (recursive)  `[easy]`

Implement factorial using direct recursion (without `math.factorial`). Document the base case explicitly.

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

## Constraints

- `0 <= n <= 500` (Python's recursion limit forbids much more without tweaking).


## Hint

<details>
<summary>Hint</summary>

Base case `n == 0` returns `1`. Otherwise `n * factorial(n - 1)`.
</details>
