from collections import Counter


def largest_component_size(nums: list[int]) -> int:
    parent: dict = {}
    def find(x):
        if parent.setdefault(x, x) != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        parent[find(x)] = find(y)

    for n in nums:
        x = n
        i = 2
        while i * i <= x:
            if x % i == 0:
                union(n, i)
                while x % i == 0:
                    x //= i
            i += 1
        if x > 1:
            union(n, x)

    groups = Counter(find(n) for n in nums)
    return max(groups.values())
