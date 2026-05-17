# 10. Furthest building you can reach  `[medium]`

Given `heights`, `bricks`, and `ladders`, jump from building 0 forward. Going down is free. Going up by `h` costs either `h` bricks or 1 ladder. Return the furthest building index you can reach.

## Function signature

```python
def furthest_building(heights: list[int], bricks: int, ladders: int) -> int: ...
```

## Examples

| heights | bricks | ladders | result |
|---|---|---|---|
| `[4, 2, 7, 6, 9, 14, 12]` | 5 | 1 | 4 |
| `[14, 3, 19, 3]` | 17 | 0 | 3 |



## Hint

<details>
<summary>Hint</summary>

Use ladders for the largest jumps; bricks for the rest. Maintain a min-heap of size `ladders` of recent jumps; whenever bigger than top, replace and spend bricks on the popped one.
</details>
