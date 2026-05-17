def eventual_safe_nodes(graph: list[list[int]]) -> list[int]:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * len(graph)

    def _safe(u: int) -> bool:
        if color[u] == GRAY:
            return False
        if color[u] == BLACK:
            return True
        color[u] = GRAY
        for v in graph[u]:
            if not _safe(v):
                return False
        color[u] = BLACK
        return True

    return [u for u in range(len(graph)) if _safe(u)]
