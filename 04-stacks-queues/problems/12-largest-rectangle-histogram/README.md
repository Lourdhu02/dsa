# 12. Largest rectangle in histogram  `[hard]`

Given an array `heights` of bar heights (each width 1), return the area of the largest rectangle in the histogram.

## Function signature

```python
def largest_rectangle(heights: list[int]) -> int: ...
```

## Examples

| heights | answer |
|---|---|
| `[2, 1, 5, 6, 2, 3]` | 10 |
| `[2, 4]` | 4 |
| `[1]` | 1 |



## Hint

<details>
<summary>Hint</summary>

Monotonic stack of bar indices, increasing in height. When a shorter bar arrives, pop and compute the rectangle that ends just before this bar with the popped bar as the smallest. Pad with a 0-height sentinel.
</details>
