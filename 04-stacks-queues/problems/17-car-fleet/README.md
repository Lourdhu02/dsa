# 17. Car fleet  `[medium]`

`n` cars at positions `position[i]` moving toward target `T` at speeds `speed[i]`. A faster car catches a slower one to form a *fleet* (same speed, moving as one). Return the number of fleets that arrive at the target.

## Function signature

```python
def car_fleet(target: int, position: list[int], speed: list[int]) -> int: ...
```

## Examples

| target | position | speed | result |
|---|---|---|---|
| 12 | `[10,8,0,5,3]` | `[2,4,1,1,3]` | 3 |
| 10 | `[3]` | `[3]` | 1 |



## Hint

<details>
<summary>Hint</summary>

Sort cars by starting position descending. Iterate and use a stack of *arrival times*. A car forms its own fleet only if it arrives strictly later than the car in front; otherwise it merges.
</details>
