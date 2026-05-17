def exclusive_time(n: int, logs: list[str]) -> list[int]:
    res = [0] * n
    stack: list[int] = []
    prev = 0
    for entry in logs:
        parts = entry.split(":")
        fid, kind, t = int(parts[0]), parts[1], int(parts[2])
        if kind == "start":
            if stack:
                res[stack[-1]] += t - prev
            stack.append(fid)
            prev = t
        else:  # end
            res[stack.pop()] += t - prev + 1
            prev = t + 1
    return res
