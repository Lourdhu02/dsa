def longest_consecutive(nums: list[int]) -> int:
    s = set(nums)
    parent: dict = {v: v for v in s}
    size: dict = {v: 1 for v in s}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        parent[ry] = rx
        size[rx] += size[ry]
    for v in s:
        if v + 1 in parent:
            union(v, v + 1)
    return max(size[find(v)] for v in s) if s else 0
