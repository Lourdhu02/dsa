# 11. Asteroid collision  `[medium]`

Given an array `asteroids` of nonzero integers where positive values move right and negative values move left at the same speed, simulate collisions. Two asteroids in collision: the smaller (by absolute value) explodes; equal-sized both explode. Return the final state.

## Function signature

```python
def asteroid_collision(asteroids: list[int]) -> list[int]: ...
```

## Examples

| input | output |
|---|---|
| `[5, 10, -5]` | `[5, 10]` |
| `[8, -8]` | `[]` |
| `[10, 2, -5]` | `[10]` |
| `[-2, -1, 1, 2]` | `[-2, -1, 1, 2]` |



## Hint

<details>
<summary>Hint</summary>

Stack. Push each asteroid; if the top is positive and the new one is negative, resolve collisions until stable.
</details>
