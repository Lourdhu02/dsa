import heapq


def smallest_range(nums: list[list[int]]) -> list[int]:
    h: list[tuple[int, int, int]] = []
    cur_max = float("-inf")
    for i, lst in enumerate(nums):
        heapq.heappush(h, (lst[0], i, 0))
        cur_max = max(cur_max, lst[0])
    best: list[int] = [-10**9, 10**9]
    while h:
        v, i, j = heapq.heappop(h)
        if cur_max - v < best[1] - best[0]:
            best = [v, cur_max]
        if j + 1 == len(nums[i]):
            break
        nxt = nums[i][j + 1]
        cur_max = max(cur_max, nxt)
        heapq.heappush(h, (nxt, i, j + 1))
    return best
