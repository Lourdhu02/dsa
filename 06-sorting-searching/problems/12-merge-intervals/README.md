# 12. Merge intervals  `[medium]`

Given an array of `intervals` where `intervals[i] = [start, end]`, merge overlapping intervals.

## Function signature

```python
def merge(intervals: list[list[int]]) -> list[list[int]]: ...
```

## Examples

| intervals | result |
|---|---|
| `[[1,3],[2,6],[8,10],[15,18]]` | `[[1,6],[8,10],[15,18]]` |
| `[[1,4],[4,5]]` | `[[1,5]]` |



## Hint

<details>
<summary>Hint</summary>

Sort by start. Walk; if current.start <= last.end, extend last; else append.
</details>
