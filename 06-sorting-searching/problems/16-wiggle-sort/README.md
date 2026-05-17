# 16. Wiggle sort  `[medium]`

Reorder `nums` such that `nums[0] <= nums[1] >= nums[2] <= nums[3] ...`. In place; `Θ(n)`.

## Function signature

```python
def wiggle_sort(nums: list[int]) -> None: ...
```

## Examples

| input | a valid output |
|---|---|
| `[3, 5, 2, 1, 6, 4]` | `[3, 5, 1, 6, 2, 4]` |
| `[1, 2, 3, 4]` | `[1, 3, 2, 4]` |



## Hint

<details>
<summary>Hint</summary>

Walk left to right. At each index, if the local order is wrong (e.g. at even index `nums[i] > nums[i+1]`), swap. Local swap preserves the prefix invariant.
</details>
