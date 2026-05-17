# 11. Rotate array  `[medium]`

Rotate the array to the **right** by `k` steps, where `k >= 0`. In place, `O(1)` extra space.

```
[1,2,3,4,5,6,7]  k=3  ->  [5,6,7,1,2,3,4]
```

The clean trick: reverse the whole array, then reverse the first `k` elements, then reverse the rest. Three passes, no aux array.

## Function signature

```python
def rotate(nums: list[int], k: int) -> None: ...
```

## Examples

| nums | k | result |
|---|---|---|
| `[1,2,3,4,5,6,7]` | 3 | `[5,6,7,1,2,3,4]` |
| `[-1,-100,3,99]` | 2 | `[3,99,-1,-100]` |
| `[1]` | 5 | `[1]` |

## Hint

<details>
<summary>Hint</summary>

`k %= len(nums)`. Reverse `nums[0:n]`, then `nums[0:k]`, then `nums[k:n]`. Why this works: the right-rotation by `k` maps index `i` to `(i + k) % n`; the three reverses compose to exactly that permutation.
</details>
