def count_inversions(nums: list[int]) -> int:
    """Time: Θ(n log n).  Space: Θ(n)."""
    def _sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, cl = _sort(a[:mid])
        right, cr = _sort(a[mid:])
        merged = []
        i = j = 0
        inv = cl + cr
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    _, total = _sort(nums)
    return total
