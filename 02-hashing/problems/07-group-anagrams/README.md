# 07. Group anagrams  `[medium]`

Given an array of strings, group anagrams together. Return the groups in any order; within a group, preserve any order.

## Function signature

```python
def group_anagrams(strs: list[str]) -> list[list[str]]: ...
```

## Examples

| strs | groups (any order) |
|---|---|
| `["eat","tea","tan","ate","nat","bat"]` | `[["bat"], ["nat","tan"], ["ate","eat","tea"]]` |
| `[""]` | `[[""]]` |
| `["a"]` | `[["a"]]` |



## Hint

<details>
<summary>Hint</summary>

Use sorted-tuple of characters as canonical form. Hash to a `dict[tuple, list[str]]`.
</details>
