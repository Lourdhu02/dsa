# 06. Middle of the linked list  `[easy]`

Return the middle node of a singly-linked list. If there are two middle nodes (even length), return the second.

## Function signature

```python
def middle_node(head: ListNode | None) -> ListNode | None: ...
```

## Examples

| input | result |
|---|---|
| `1->2->3->4->5` | node with value 3 |
| `1->2->3->4->5->6` | node with value 4 |



## Hint

<details>
<summary>Hint</summary>

Fast/slow. Slow moves 1, fast moves 2. When fast reaches end, slow is the middle.
</details>
