# 14. Reorder list  `[medium]`

Given `L0 -> L1 -> ... -> Ln-1`, reorder in place to `L0 -> Ln-1 -> L1 -> Ln-2 -> L2 -> Ln-3 -> ...`. `Θ(n)` time, `Θ(1)` extra space.

## Function signature

```python
def reorder_list(head: ListNode | None) -> None: ...
```

## Examples

| input | result |
|---|---|
| `1->2->3->4` | `1->4->2->3` |
| `1->2->3->4->5` | `1->5->2->4->3` |



## Hint

<details>
<summary>Hint</summary>

1. Find the midpoint (fast/slow). 2. Reverse the second half. 3. Interleave the two halves.
</details>
