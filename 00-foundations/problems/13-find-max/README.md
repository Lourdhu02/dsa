# 13. Find max  `[easy]`

Return the maximum element of a non-empty list of integers.

The point is the **loop invariant** — write it as a comment in your solution.

## Function signature

```python
def find_max(xs: list[int]) -> int: ...
```

## Examples

| xs | max |
|---|---|
| `[3]` | 3 |
| `[-1, -2, -3]` | -1 |
| `[5, 1, 5, 1]` | 5 |
| `[1, 2, 3, 4, 5]` | 5 |

## Constraints

- `1 <= len(xs) <= 10^6`

## Hint

<details>
<summary>Hint</summary>

Initialize `best = xs[0]`. Invariant: after iteration `i`, `best == max(xs[0:i+1])`. Update on each step. Raise on empty input.
</details>
