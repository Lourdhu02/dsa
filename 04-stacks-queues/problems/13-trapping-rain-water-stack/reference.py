def trap(height: list[int]) -> int:
    """Time: Θ(n).  Space: Θ(n).  Compare to module 01's two-pointer Θ(1) space version."""
    stack: list[int] = []
    total = 0
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if not stack:
                break
            left = stack[-1]
            width = i - left - 1
            bounded = min(height[left], h) - height[bottom]
            total += width * bounded
        stack.append(i)
    return total
