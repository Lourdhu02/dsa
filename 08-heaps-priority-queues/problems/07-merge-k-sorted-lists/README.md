# 07. Merge k sorted lists  `[hard]`

Given `k` sorted linked lists, merge them into one sorted linked list and return its head.

## Function signature

```python
class ListNode: ...

def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None: ...
```

## Examples

```
input: [[1,4,5],[1,3,4],[2,6]]
output: 1->1->2->3->4->4->5->6
```



## Hint

<details>
<summary>Hint</summary>

Min-heap of (value, list_idx, node). Pop the smallest, advance that list.
</details>
