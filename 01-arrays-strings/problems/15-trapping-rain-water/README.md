# 15. Trapping rain water  `[hard]`

Given `n` non-negative integers representing an elevation map where bar `i` has height `height[i]`, compute how much water can be trapped after raining.

```
heights = [0,1,0,2,1,0,1,3,2,1,2,1]  -> 6 units of water trapped
```

## Function signature

```python
def trap(height: list[int]) -> int: ...
```

## Examples

| height | trapped |
|---|---|
| `[0,1,0,2,1,0,1,3,2,1,2,1]` | 6 |
| `[4,2,0,3,2,5]` | 9 |
| `[]` | 0 |
| `[3]` | 0 |

## Hint

<details>
<summary>Hint</summary>

For each position `i`, water level = `min(maxLeft[i], maxRight[i])`. Compute those two arrays (prefix and suffix maxes), then sum `level - height[i]`.

`O(1)` space version: two pointers. Maintain `left_max`, `right_max`. Move the side with the smaller bar inward; water there is capped by the smaller running max (the other side guarantees a taller barrier).
</details>

## Two valid approaches

| Approach | Time | Space |
|---|---|---|
| Prefix-max + suffix-max | Θ(n) | Θ(n) |
| Two pointers | Θ(n) | Θ(1) |
| Monotonic stack | Θ(n) | Θ(n) (covered in module 04) |
