def daily_temperatures(temps: list[int]) -> list[int]:
    n = len(temps)
    res = [0] * n
    stack: list[int] = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res
