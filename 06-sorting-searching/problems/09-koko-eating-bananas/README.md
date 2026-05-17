# 09. Koko eating bananas  `[medium]`

Koko eats `k` bananas per hour from one pile. If a pile has fewer than `k`, she still spends a full hour. Given `piles` and `h` hours, return the minimum `k` such that she finishes within `h` hours.

## Function signature

```python
def min_eating_speed(piles: list[int], h: int) -> int: ...
```

## Examples

| piles | h | result |
|---|---|---|
| `[3, 6, 7, 11]` | 8 | 4 |
| `[30, 11, 23, 4, 20]` | 5 | 30 |



## Hint

<details>
<summary>Hint</summary>

Binary-search the smallest k in `[1, max(piles)]` with `sum(ceil(p/k) for p in piles) <= h`.
</details>
