# 04. Course schedule  `[medium]`

There are `num_courses` courses labeled `0..num_courses-1`. `prereqs[i] = [a, b]` means take `b` before `a`. Return True if you can finish all courses.

## Function signature

```python
def can_finish(num_courses: int, prereqs: list[list[int]]) -> bool: ...
```

## Examples

| num_courses | prereqs | result |
|---|---|---|
| 2 | `[[1, 0]]` | True |
| 2 | `[[1, 0], [0, 1]]` | False |



## Hint

<details>
<summary>Hint</summary>

Kahn's algorithm. If topological order has length < num_courses, there's a cycle.
</details>
