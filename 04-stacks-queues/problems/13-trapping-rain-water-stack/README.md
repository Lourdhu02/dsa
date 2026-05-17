# 13. Trapping rain water (monotonic stack)  `[hard]`

Same problem as module 01 problem 15, but implement using a monotonic stack so you internalize the second canonical pattern.

## Function signature

```python
def trap(height: list[int]) -> int: ...
```

## Examples

| height | trapped |
|---|---|
| `[0,1,0,2,1,0,1,3,2,1,2,1]` | 6 |
| `[4,2,0,3,2,5]` | 9 |



## Hint

<details>
<summary>Hint</summary>

Stack of indices in decreasing height. On a new bar that is taller than the top, pop the top, compute trapped water between the new top of the stack and the new bar, bounded by min of their heights.
</details>
