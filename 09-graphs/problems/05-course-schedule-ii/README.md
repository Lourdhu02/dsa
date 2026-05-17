# 05. Course schedule II  `[medium]`

Same as course-schedule but return a valid course order, or `[]` if impossible.

## Function signature

```python
def find_order(num_courses: int, prereqs: list[list[int]]) -> list[int]: ...
```

## Examples

| n | prereqs | one valid order |
|---|---|---|
| 4 | `[[1, 0], [2, 0], [3, 1], [3, 2]]` | `[0, 1, 2, 3]` |
| 2 | `[[0, 1], [1, 0]]` | `[]` |



## Hint

<details>
<summary>Hint</summary>

Kahn's; return the emitted order.
</details>
