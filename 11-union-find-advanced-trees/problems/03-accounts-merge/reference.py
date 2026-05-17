from collections import defaultdict


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    n = len(accounts)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    email_to_idx: dict[str, int] = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in email_to_idx:
                union(email_to_idx[email], i)
            email_to_idx[email] = i

    groups: dict[int, list[str]] = defaultdict(list)
    for email, idx in email_to_idx.items():
        groups[find(idx)].append(email)
    return [[accounts[r][0]] + sorted(emails) for r, emails in groups.items()]
