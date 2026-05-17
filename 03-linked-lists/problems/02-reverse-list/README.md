# 02. Reverse a linked list  `[easy]`

Given the head of a singly-linked list, reverse the list in place and return the new head. `Θ(n)` time, `Θ(1)` extra space.

## Function signature

```python
def reverse_list(head: ListNode | None) -> ListNode | None: ...
```

## Examples

| input | output |
|---|---|
| `1 -> 2 -> 3 -> 4 -> 5` | `5 -> 4 -> 3 -> 2 -> 1` |
| `1 -> 2` | `2 -> 1` |
| `[]` | `[]` |



## Hint

<details>
<summary>Hint</summary>

Three pointers: `prev=None, curr=head`. On each step, save `nxt = curr.next`, set `curr.next = prev`, advance `prev = curr; curr = nxt`.
</details>
