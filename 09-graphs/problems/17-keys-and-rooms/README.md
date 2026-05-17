# 17. Keys and rooms  `[medium]`

Rooms 0..n-1; room i contains keys `rooms[i]`. You start in room 0. Return True if you can visit all rooms.

## Function signature

```python
def can_visit_all_rooms(rooms: list[list[int]]) -> bool: ...
```

## Examples

`[[1], [2], [3], []]` → True.
`[[1, 3], [3, 0, 1], [2], [0]]` → False (room 2 has key only for itself).



## Hint

<details>
<summary>Hint</summary>

DFS/BFS starting at room 0; check that the visited set equals `range(n)`.
</details>
