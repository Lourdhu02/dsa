def count_smaller(nums: list[int]) -> list[int]:
    """Time: Θ(n log n).  Space: Θ(n)."""
    n = len(nums)
    counts = [0] * n
    idxs = list(range(n))

    def _sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = _sort(arr[:mid])
        right = _sort(arr[mid:])
        merged = []
        i = j = 0
        right_used = 0
        while i < len(left) and j < len(right):
            if nums[left[i]] <= nums[right[j]]:
                counts[left[i]] += right_used
                merged.append(left[i])
                i += 1
            else:
                right_used += 1
                merged.append(right[j])
                j += 1
        while i < len(left):
            counts[left[i]] += right_used
            merged.append(left[i])
            i += 1
        merged.extend(right[j:])
        return merged

    _sort(idxs)
    return counts
