# 14. Minimum genetic mutation  `[medium]`

Given `start_gene`, `end_gene`, and a `bank` of valid genes (8-character strings of A,C,G,T), return the minimum number of single-character mutations to go from start to end through bank-only intermediates. -1 if impossible.

## Function signature

```python
def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int: ...
```

## Examples

| start | end | bank | result |
|---|---|---|---|
| `"AACCGGTT"` | `"AACCGGTA"` | `["AACCGGTA"]` | 1 |
| `"AACCGGTT"` | `"AAACGGTA"` | `["AACCGGTA","AACCGCTA","AAACGGTA"]` | 2 |



## Hint

<details>
<summary>Hint</summary>

Treat each gene as a node, edges between bank genes that differ by one char. BFS.
</details>
