# 05. Gas station  `[medium]`

Given `gas[i]` and `cost[i]` arrays around a circle of gas stations, return the starting index that lets you complete the loop, or -1.

## Function signature

```python
def can_complete_circuit(gas: list[int], cost: list[int]) -> int: ...
```

## Examples

| gas | cost | result |
|---|---|---|
| `[1,2,3,4,5]` | `[3,4,5,1,2]` | 3 |
| `[2,3,4]` | `[3,4,3]` | -1 |



## Hint

<details>
<summary>Hint</summary>

If total gas < total cost: -1. Otherwise the answer is the position right after the running tank dipped to its minimum.
</details>
