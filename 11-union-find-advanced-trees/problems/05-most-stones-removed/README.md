# 05. Most stones removed with same row or column  `[medium]`

Given `stones` (list of `[r, c]` coords), you can remove a stone if it shares a row or column with another remaining stone. Return the max number you can remove.

## Function signature

```python
def remove_stones(stones: list[list[int]]) -> int: ...
```

## Examples

| stones | result |
|---|---|
| `[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]` | 5 |
| `[[0,0],[0,2],[1,1],[2,0],[2,2]]` | 3 |



## Hint

<details>
<summary>Hint</summary>

Two stones sharing row OR column are in the same component (union them). Answer = `n - num_components`.
</details>
