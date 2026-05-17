def all_paths(graph: list[list[int]]) -> list[list[int]]:
    out: list[list[int]] = []
    target = len(graph) - 1
    path: list[int] = [0]

    def _dfs(u: int) -> None:
        if u == target:
            out.append(path[:])
            return
        for v in graph[u]:
            path.append(v)
            _dfs(v)
            path.pop()

    _dfs(0)
    return out
