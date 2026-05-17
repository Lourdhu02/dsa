# 11. Remove duplicates from sorted list  `[easy]`

Given a sorted singly-linked list, remove duplicates so each element appears only once. Return the modified head.

## Function signature

```python
def delete_duplicates(head: ListNode | None) -> ListNode | None: ...
```

## Examples

| input | result |
|---|---|
| `1->1->2` | `1->2` |
| `1->1->2->3->3` | `1->2->3` |



## Hint

<details>
<summary>Hint</summary>

Walk once. If `cur.next.val == cur.val`, skip: `cur.next = cur.next.next`. Else advance.
</details>
