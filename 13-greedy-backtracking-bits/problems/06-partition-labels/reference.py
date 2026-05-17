def partition_labels(s: str) -> list[int]:
    last = {ch: i for i, ch in enumerate(s)}
    out: list[int] = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            out.append(end - start + 1)
            start = i + 1
    return out
