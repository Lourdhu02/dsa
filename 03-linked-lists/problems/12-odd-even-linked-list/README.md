# 12. Odd-even linked list  `[medium]`

Reorder a singly-linked list so that all nodes at odd positions (1-indexed) come before all nodes at even positions, preserving relative order within each group. `Θ(n)` time, `Θ(1)` extra space.

## Function signature

```python
def odd_even_list(head: ListNode | None) -> ListNode | None: ...
```

## Examples

| input | result |
|---|---|
| `1->2->3->4->5` | `1->3->5->2->4` |
| `2->1->3->5->6->4->7` | `2->3->6->7->1->5->4` |



## Hint

<details>
<summary>Hint</summary>

Maintain two chains: odd-position tail and even-position tail. Walk through the list, pulling alternating nodes into each chain. Finally, set `odd.next = even_head`.
</details>
