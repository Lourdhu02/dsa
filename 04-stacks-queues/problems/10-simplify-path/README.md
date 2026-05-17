# 10. Simplify path  `[medium]`

Given a Unix-style absolute path, return its canonical form: collapse `.`, `..`, and consecutive slashes.

## Function signature

```python
def simplify_path(path: str) -> str: ...
```

## Examples

| path | result |
|---|---|
| `"/home/"` | `"/home"` |
| `"/../"` | `"/"` |
| `"/home//foo/"` | `"/home/foo"` |
| `"/a/./b/../../c/"` | `"/c"` |



## Hint

<details>
<summary>Hint</summary>

Split by `/`. For each piece: skip empty/`.`, pop on `..`, push otherwise.
</details>
