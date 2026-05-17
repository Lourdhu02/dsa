# 04. Move zeros to the end  `[easy]`

Given an integer array, move all `0`s to the end **in place** while preserving the relative order of the non-zero elements. `O(1)` extra space.

## Function signature

```python
def move_zeros(nums: list[int]) -> None: ...
```

## Examples

| input | result |
|---|---|
| `[0, 1, 0, 3, 12]` | `[1, 3, 12, 0, 0]` |
| `[0]` | `[0]` |
| `[1, 2, 3]` | `[1, 2, 3]` |

## Hint

<details>
<summary>Hint</summary>

Same-direction two pointers. Fast scans; slow points to the next slot for the next non-zero. Swap `nums[slow]` and `nums[fast]` whenever `nums[fast] != 0` so trailing zeros end up at the back.
</details>
