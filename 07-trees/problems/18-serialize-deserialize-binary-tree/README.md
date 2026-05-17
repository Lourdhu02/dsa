# 18. Serialize and deserialize binary tree  `[hard]`

Design `serialize(root) -> str` and `deserialize(s) -> root` such that `deserialize(serialize(t))` reproduces the original tree.

## Function signature

```python
class Codec:
    def serialize(self, root: TreeNode | None) -> str: ...
    def deserialize(self, data: str) -> TreeNode | None: ...
```

## Examples

Any reversible encoding works. Suggested: level-order with `"null"` for missing children, comma-separated.



## Hint

<details>
<summary>Hint</summary>

BFS for serialize. For deserialize, parse tokens, build the root, then a queue of parents — for each parent, consume 2 tokens (left, right).
</details>
