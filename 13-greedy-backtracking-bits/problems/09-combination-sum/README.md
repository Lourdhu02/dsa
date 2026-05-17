# 09. Combination sum (unbounded reuse)  `[medium]`

Given distinct positive `candidates` and a `target`, return all unique combinations (each candidate may be used unlimited times) that sum to target.

## Function signature

```python
def combination_sum(candidates: list[int], target: int) -> list[list[int]]: ...
```

## Examples

| candidates | target | result |
|---|---|---|
| `[2, 3, 6, 7]` | 7 | `[[2, 2, 3], [7]]` |



## Hint

<details>
<summary>Hint</summary>

Backtrack with start index (don't go back). Avoid duplicates by always advancing or staying at start.
</details>
