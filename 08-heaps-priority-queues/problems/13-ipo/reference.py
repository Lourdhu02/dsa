import heapq


def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    by_cap = sorted(zip(capital, profits))
    affordable: list[int] = []
    i = 0
    for _ in range(k):
        while i < len(by_cap) and by_cap[i][0] <= w:
            heapq.heappush(affordable, -by_cap[i][1])
            i += 1
        if not affordable:
            break
        w += -heapq.heappop(affordable)
    return w
