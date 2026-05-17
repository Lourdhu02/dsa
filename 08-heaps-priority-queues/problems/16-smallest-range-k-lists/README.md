# 16. Smallest range covering elements from k lists  `[hard]`

Given `k` sorted lists of integers, find the smallest range `[a, b]` that includes at least one number from each list.

## Function signature

```python
def smallest_range(nums: list[list[int]]) -> list[int]: ...
```

## Examples

| nums | result |
|---|---|
| `[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]` | `[20, 24]` |



## Hint

<details>
<summary>Hint</summary>

Heap of one pointer per list. Track running max. After each pop, update range and advance the popped list's pointer.
</details>
