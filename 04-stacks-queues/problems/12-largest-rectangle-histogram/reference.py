def largest_rectangle(heights: list[int]) -> int:
    """Time: Θ(n) amortized.  Space: Θ(n)."""
    heights = heights + [0]
    stack: list[int] = []
    best = 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = heights[top] * width
            if area > best:
                best = area
        stack.append(i)
    return best
