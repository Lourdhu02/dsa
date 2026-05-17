# 06. Network delay time (Dijkstra)  `[medium]`

Given `n` nodes labeled `1..n`, `times[i] = [u, v, w]` is a directed edge of weight `w`. Starting at node `k`, return the time it takes for all nodes to receive the signal (max shortest path) or -1 if unreachable.

## Function signature

```python
def network_delay_time(times: list[list[int]], n: int, k: int) -> int: ...
```

## Examples

| times | n | k | result |
|---|---|---|---|
| `[[2, 1, 1], [2, 3, 1], [3, 4, 1]]` | 4 | 2 | 2 |
| `[[1, 2, 1]]` | 2 | 1 | 1 |
| `[[1, 2, 1]]` | 2 | 2 | -1 |



## Hint

<details>
<summary>Hint</summary>

Standard Dijkstra; answer = max of distances or -1 if any node unreachable.
</details>
