# 10. Capacity to ship packages within D days  `[medium]`

Given weights of packages (must ship in given order) and `days`, return the minimum ship capacity that allows shipping in `days`.

## Function signature

```python
def ship_within_days(weights: list[int], days: int) -> int: ...
```

## Examples

| weights | days | result |
|---|---|---|
| `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` | 5 | 15 |
| `[3, 2, 2, 4, 1, 4]` | 3 | 6 |
| `[1, 2, 3, 1, 1]` | 4 | 3 |



## Hint

<details>
<summary>Hint</summary>

Binary-search the smallest capacity in `[max(weights), sum(weights)]` such that greedy day-count is `<= days`.
</details>
