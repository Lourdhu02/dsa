# 06. Partition labels  `[medium]`

Given a string `s`, partition it so each letter appears in at most one part. Return the lengths of these parts.

## Function signature

```python
def partition_labels(s: str) -> list[int]: ...
```

## Examples

| s | result |
|---|---|
| `"ababcbacadefegdehijhklij"` | `[9, 7, 8]` |
| `"eccbbbbdec"` | `[10]` |



## Hint

<details>
<summary>Hint</summary>

Map char -> last index. Walk while tracking `end = max(end, last[s[i]])`. When i == end, record length and reset start.
</details>
