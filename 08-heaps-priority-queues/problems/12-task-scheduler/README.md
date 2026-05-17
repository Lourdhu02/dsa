# 12. Task scheduler  `[medium]`

Given a list of CPU tasks and integer `n`, return the minimum number of time units to finish all tasks where the same task must be `n` units apart.

## Function signature

```python
def least_interval(tasks: list[str], n: int) -> int: ...
```

## Examples

| tasks | n | result |
|---|---|---|
| `["A","A","A","B","B","B"]` | 2 | 8 |
| `["A","C","A","B","D","B"]` | 1 | 6 |



## Hint

<details>
<summary>Hint</summary>

Closed-form: `max(len(tasks), (max_count - 1) * (n + 1) + tied_max)` — derivation in CP-algorithms.
</details>
