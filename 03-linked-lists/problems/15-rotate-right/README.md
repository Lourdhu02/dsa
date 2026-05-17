# 15. Rotate linked list right  `[medium]`

Rotate the list to the right by `k` places. `k` may be larger than the list length.

## Function signature

```python
def rotate_right(head: ListNode | None, k: int) -> ListNode | None: ...
```

## Examples

| input | k | result |
|---|---|---|
| `1->2->3->4->5` | 2 | `4->5->1->2->3` |
| `0->1->2` | 4 | `2->0->1` |
| `[]` | 1 | `[]` |



## Hint

<details>
<summary>Hint</summary>

Close the list into a cycle, walk `n - k % n` steps from head, break the cycle there.
</details>
