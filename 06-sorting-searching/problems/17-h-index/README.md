# 17. H-index  `[medium]`

Given citations of a researcher's papers, return the h-index: the largest `h` such that the researcher has `h` papers each cited at least `h` times.

## Function signature

```python
def h_index(citations: list[int]) -> int: ...
```

## Examples

| citations | h-index |
|---|---|
| `[3, 0, 6, 1, 5]` | 3 |
| `[1, 3, 1]` | 1 |
| `[]` | 0 |



## Hint

<details>
<summary>Hint</summary>

Counting-sort by citation count (cap at n). Then walk from highest count downward accumulating papers; first `count >= h` is the answer.
</details>
