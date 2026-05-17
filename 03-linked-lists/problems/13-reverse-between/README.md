# 13. Reverse linked list between indices  `[medium]`

Reverse the nodes of the list between positions `left` and `right` (1-indexed, inclusive). Single pass, `Θ(1)` extra space.

## Function signature

```python
def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None: ...
```

## Examples

| input | left | right | result |
|---|---|---|---|
| `1->2->3->4->5` | 2 | 4 | `1->4->3->2->5` |
| `5` | 1 | 1 | `5` |



## Hint

<details>
<summary>Hint</summary>

Use a sentinel. Walk to the node just before `left`. From there, repeatedly take `cur.next` and move it to the front of the sublist (insert after the sentinel of the sublist).
</details>
