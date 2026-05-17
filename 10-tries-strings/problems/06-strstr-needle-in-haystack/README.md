# 06. Implement strStr (needle in haystack)  `[medium]`

Given two strings, return the index of the first occurrence of `needle` in `haystack`, or -1.

## Function signature

```python
def str_str(haystack: str, needle: str) -> int: ...
```

## Examples

| haystack | needle | result |
|---|---|---|
| `"sadbutsad"` | `"sad"` | 0 |
| `"leetcode"` | `"leeto"` | -1 |



## Hint

<details>
<summary>Hint</summary>

KMP gives Θ(n+m). For interview: a Θ(n*m) naive scan is also accepted.
</details>
