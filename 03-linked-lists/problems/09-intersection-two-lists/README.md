# 09. Intersection of two linked lists  `[medium]`

Given heads of two singly-linked lists, return the node where they first intersect, or `None` if they don't. `Θ(n + m)` time, `Θ(1)` space.

## Function signature

```python
def get_intersection(a: ListNode | None, b: ListNode | None) -> ListNode | None: ...
```

## Examples

Two lists that share a suffix have an intersection node (the first shared one).



## Hint

<details>
<summary>Hint</summary>

Two pointers, each walks list A then list B (and vice versa). After at most `n + m` steps they either both reach `None` (no intersection) or land on the same node (the answer). Proof: both pointers traverse exactly `n + m` nodes total before any miss is recovered.
</details>
