def equations_possible(equations: list[str]) -> bool:
    parent = list(range(26))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for eq in equations:
        if eq[1] == "=":
            a, b = ord(eq[0]) - 97, ord(eq[3]) - 97
            parent[find(a)] = find(b)
    for eq in equations:
        if eq[1] == "!":
            a, b = ord(eq[0]) - 97, ord(eq[3]) - 97
            if find(a) == find(b):
                return False
    return True
