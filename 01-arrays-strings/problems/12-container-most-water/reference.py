def max_area(height: list[int]) -> int:
    """Converging two-pointer with exchange-argument correctness.

    Time:  Θ(n)
    Space: Θ(1)
    """
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        h = min(height[l], height[r])
        area = (r - l) * h
        if area > best:
            best = area
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best
