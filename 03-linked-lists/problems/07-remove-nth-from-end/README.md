# 07. Remove Nth node from end  `[medium]`

Given the head of a list and integer `n`, remove the `n`-th node from the end (1-indexed) and return the new head.

## Function signature

```python
def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None: ...
```

## Examples

| list | n | result |
|---|---|---|
| `1->2->3->4->5` | 2 | `1->2->3->5` |
| `1` | 1 | `[]` |
| `1->2` | 1 | `1` |



## Hint

<details>
<summary>Hint</summary>

Use a sentinel node before `head` so removing the actual head is uniform. Move `fast` n+1 steps ahead, then advance both until `fast is None`. `slow.next` is the node to remove.
</details>
