# 18. Exclusive time of functions  `[medium]`

Given the start/end logs of function calls in a single-threaded program, return the exclusive time spent in each function (time spent inside the function not counting time inside nested calls).

## Function signature

```python
def exclusive_time(n: int, logs: list[str]) -> list[int]: ...
```

## Examples

| n | logs | result |
|---|---|---|
| 2 | `["0:start:0","1:start:2","1:end:5","0:end:6"]` | `[3, 4]` |



## Hint

<details>
<summary>Hint</summary>

Stack of currently active function ids. On `start`, charge elapsed time to the function on top of stack, then push. On `end`, charge elapsed time to the function being popped.
</details>
