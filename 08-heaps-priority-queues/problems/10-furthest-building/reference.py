import heapq


def furthest_building(heights: list[int], bricks: int, ladders: int) -> int:
    h: list[int] = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        heapq.heappush(h, diff)
        if len(h) > ladders:
            bricks -= heapq.heappop(h)
            if bricks < 0:
                return i
    return len(heights) - 1
