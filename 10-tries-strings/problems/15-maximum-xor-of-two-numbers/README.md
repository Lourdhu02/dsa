# 15. Maximum XOR of two numbers (binary trie)  `[medium]`

Given a list of non-negative integers, return the max XOR of any two of them. Solve in `Θ(n · 32)`.

## Function signature

```python
def find_maximum_xor(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[3, 10, 5, 25, 2, 8]` | 28 |
| `[0]` | 0 |



## Hint

<details>
<summary>Hint</summary>

Bitwise trie of the 32-bit representations. For each number, walk the trie greedily picking opposite bits to maximize XOR.
</details>
