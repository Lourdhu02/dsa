def remove_stones(stones: list[list[int]]) -> int:
    parent: dict = {}

    def find(x):
        if parent.get(x, x) == x:
            parent[x] = x
            return x
        root = find(parent[x])
        parent[x] = root
        return root

    def union(x, y):
        parent[find(x)] = find(y)

    for r, c in stones:
        union(("r", r), ("c", c))

    roots = {find(("r", r)) for r, _ in stones}
    return len(stones) - len(roots)
