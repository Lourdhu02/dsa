# 06. K closest points to origin  `[medium]`

Return the k points in `points` closest to the origin by Euclidean distance.

## Function signature

```python
def k_closest(points: list[list[int]], k: int) -> list[list[int]]: ...
```

## Examples

| points | k | result |
|---|---|---|
| `[[1, 3], [-2, 2]]` | 1 | `[[-2, 2]]` |
| `[[3, 3], [5, -1], [-2, 4]]` | 2 | `[[3, 3], [-2, 4]]` |



## Hint

<details>
<summary>Hint</summary>

Max-heap of size k keyed by squared distance.
</details>
