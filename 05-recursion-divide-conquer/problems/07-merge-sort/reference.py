def merge_sort(xs: list[int]) -> list[int]:
    """Time: Θ(n log n).  Space: Θ(n).  Stable.  Reference: CLRS § 2.3."""
    if len(xs) <= 1:
        return xs[:]
    mid = len(xs) // 2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])
    out: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
