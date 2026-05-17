from collections import deque


def find_order(num_courses: int, prereqs: list[list[int]]) -> list[int]:
    indeg = [0] * num_courses
    adj: list[list[int]] = [[] for _ in range(num_courses)]
    for a, b in prereqs:
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    out: list[int] = []
    while q:
        u = q.popleft()
        out.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return out if len(out) == num_courses else []
