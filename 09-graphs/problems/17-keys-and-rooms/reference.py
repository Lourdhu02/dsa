def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for k in rooms[u]:
            if k not in seen:
                seen.add(k)
                stack.append(k)
    return len(seen) == len(rooms)
