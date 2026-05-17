from bisect import bisect_left, bisect_right


def count_range_sum(nums: list[int], lower: int, upper: int) -> int:
    P = [0]
    for x in nums:
        P.append(P[-1] + x)

    def _sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, cl = _sort(arr[:mid])
        right, cr = _sort(arr[mid:])
        cnt = cl + cr
        for x in left:
            lo = bisect_left(right, x + lower)
            hi = bisect_right(right, x + upper)
            cnt += hi - lo
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged, cnt

    _, total = _sort(P)
    return total
