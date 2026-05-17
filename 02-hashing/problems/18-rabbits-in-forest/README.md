# 18. Rabbits in the forest  `[medium]`

Each rabbit reports `answers[i]` — the number of OTHER rabbits with the same color. Return the minimum total number of rabbits in the forest consistent with the answers.

## Function signature

```python
def num_rabbits(answers: list[int]) -> int: ...
```

## Examples

| answers | result |
|---|---|
| `[1, 1, 2]` | 5 |
| `[10, 10, 10]` | 11 |
| `[]` | 0 |



## Hint

<details>
<summary>Hint</summary>

Rabbits with answer `a` come in groups of size `a+1`. Count how many rabbits gave each answer `a`; ceil-divide by `a+1` to get the number of groups; multiply each group by `a+1` to get total rabbits.
</details>
