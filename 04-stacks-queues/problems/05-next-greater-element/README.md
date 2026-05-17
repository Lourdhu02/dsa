# 05. Next greater element  `[medium]`

Given array `nums`, return an array where `out[i]` is the next strictly greater element of `nums` to the right of index `i`, or `-1` if none.

## Function signature

```python
def next_greater(nums: list[int]) -> list[int]: ...
```

## Examples

| nums | result |
|---|---|
| `[2, 1, 2, 4, 3]` | `[4, 2, 4, -1, -1]` |
| `[1, 2, 3, 4]` | `[2, 3, 4, -1]` |
| `[4, 3, 2, 1]` | `[-1, -1, -1, -1]` |



## Hint

<details>
<summary>Hint</summary>

Monotonic stack of indices, non-increasing from bottom to top.
</details>
