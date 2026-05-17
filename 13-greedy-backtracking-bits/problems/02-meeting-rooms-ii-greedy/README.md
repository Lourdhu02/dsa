# 02. Meeting rooms II (greedy + heap)  `[medium]`

Same as module 06 #14 — included to drill the greedy/heap perspective.

## Function signature

```python
def min_meeting_rooms(intervals: list[list[int]]) -> int: ...
```

## Examples

| intervals | rooms |
|---|---|
| `[[0, 30], [5, 10], [15, 20]]` | 2 |



## Hint

<details>
<summary>Hint</summary>

Sort by start; min-heap of end times.
</details>
