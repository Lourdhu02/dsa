# 08. Combinations (backtracking)  `[medium]`

Return all `k`-element subsets of `{1, 2, ..., n}`.

## Function signature

```python
def combine(n: int, k: int) -> list[list[int]]: ...
```

## Examples

| n | k | count |
|---|---|---|
| 4 | 2 | 6 |



## Hint

<details>
<summary>Hint</summary>

Backtrack with start index. Prune via `for i in range(start, n - (k - len(path)) + 2)`.
</details>
