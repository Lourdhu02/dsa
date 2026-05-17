# 16. Copy list with random pointer  `[medium]`

Each node has `next` and `random` pointers (random may point to any node or None). Return a deep copy of the list.

## Function signature

```python
class Node:
    val: int
    next: 'Node | None'
    random: 'Node | None'

def copy_random_list(head: Node | None) -> Node | None: ...
```

## Examples

```
1 -> 2 -> 3
|    |
random=3  random=1
```

Output: an independent copy with the same structure.



## Hint

<details>
<summary>Hint</summary>

Two-pass with hash map: pass 1 builds a map `original_node -> cloned_node` for every node. Pass 2 wires `next` and `random` of each clone using the map.
</details>
