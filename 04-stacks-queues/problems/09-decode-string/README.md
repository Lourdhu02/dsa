# 09. Decode string  `[medium]`

Given an encoded string like `3[a]2[bc]`, decode it to `"aaabcbc"`. Encoding rule: `k[encoded_string]` repeats `encoded_string` exactly `k` times. Brackets can nest.

## Function signature

```python
def decode_string(s: str) -> str: ...
```

## Examples

| s | decoded |
|---|---|
| `"3[a]2[bc]"` | `"aaabcbc"` |
| `"3[a2[c]]"` | `"accaccacc"` |
| `"2[abc]3[cd]ef"` | `"abcabccdcdcdef"` |



## Hint

<details>
<summary>Hint</summary>

Two stacks: one for repeat counts, one for partially-built strings. On `[`, push the current count and current string; reset. On `]`, pop and combine.
</details>
