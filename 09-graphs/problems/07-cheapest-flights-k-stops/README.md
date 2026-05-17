# 07. Cheapest flights within K stops  `[medium]`

Given `n` cities, `flights[i] = [from, to, price]`, find the cheapest price from `src` to `dst` with at most `k` stops, or -1.

## Function signature

```python
def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int: ...
```

## Examples

| n | flights | src | dst | k | result |
|---|---|---|---|---|---|
| 3 | `[[0, 1, 100], [1, 2, 100], [0, 2, 500]]` | 0 | 2 | 1 | 200 |
| 3 | same | 0 | 2 | 0 | 500 |



## Hint

<details>
<summary>Hint</summary>

Bellman-Ford for `k + 1` iterations; updates only from the previous round's distances.
</details>
