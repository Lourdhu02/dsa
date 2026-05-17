import heapq
from collections import Counter


def reorganize_string(s: str) -> str:
    counts = Counter(s)
    if max(counts.values()) > (len(s) + 1) // 2:
        return ""
    h = [(-c, ch) for ch, c in counts.items()]
    heapq.heapify(h)
    out: list[str] = []
    prev_c, prev_ch = 0, ""
    while h:
        c, ch = heapq.heappop(h)
        out.append(ch)
        if prev_c < 0:
            heapq.heappush(h, (prev_c, prev_ch))
        prev_c, prev_ch = c + 1, ch
    return "".join(out)
