# 13. Insert interval  `[medium]`

You have a set of non-overlapping intervals sorted by start. Insert a new interval, merging overlaps. `Θ(n)`.

## Function signature

```python
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]: ...
```

## Examples

| intervals | new | result |
|---|---|---|
| `[[1,3],[6,9]]` | `[2,5]` | `[[1,5],[6,9]]` |
| `[[1,2],[3,5],[6,7],[8,10],[12,16]]` | `[4,8]` | `[[1,2],[3,10],[12,16]]` |



## Hint

<details>
<summary>Hint</summary>

Single pass: pass through intervals that end before new starts; merge those that overlap; append the rest.
</details>
