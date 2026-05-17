# 14. Meeting rooms II  `[medium]`

Given an array of meeting time intervals, return the minimum number of conference rooms required.

## Function signature

```python
def min_meeting_rooms(intervals: list[list[int]]) -> int: ...
```

## Examples

| intervals | result |
|---|---|
| `[[0, 30], [5, 10], [15, 20]]` | 2 |
| `[[7, 10], [2, 4]]` | 1 |



## Hint

<details>
<summary>Hint</summary>

Sort starts and ends separately. Sweep: each start increments room count; each end decrements. Track max.
</details>
