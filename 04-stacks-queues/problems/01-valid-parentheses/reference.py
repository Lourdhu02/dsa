def is_valid(s: str) -> bool:
    """Time: Θ(n).  Space: Θ(n)."""
    match = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in match.values():
            stack.append(ch)
        else:
            if not stack or stack.pop() != match[ch]:
                return False
    return not stack
