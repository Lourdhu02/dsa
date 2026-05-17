from collections import defaultdict


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    adj: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for (a, b), v in zip(equations, values):
        adj[a].append((b, v))
        adj[b].append((a, 1.0 / v))

    def _query(src: str, dst: str) -> float:
        if src not in adj or dst not in adj:
            return -1.0
        if src == dst:
            return 1.0
        seen = {src}
        stack = [(src, 1.0)]
        while stack:
            u, prod = stack.pop()
            if u == dst:
                return prod
            for v, w in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append((v, prod * w))
        return -1.0

    return [_query(c, d) for c, d in queries]
