from collections import deque


def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int:
    bank_set = set(bank)
    if end_gene not in bank_set:
        return -1
    seen = {start_gene}
    q = deque([(start_gene, 0)])
    while q:
        gene, d = q.popleft()
        if gene == end_gene:
            return d
        for i in range(len(gene)):
            for ch in "ACGT":
                if ch == gene[i]:
                    continue
                nxt = gene[:i] + ch + gene[i + 1:]
                if nxt in bank_set and nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, d + 1))
    return -1
