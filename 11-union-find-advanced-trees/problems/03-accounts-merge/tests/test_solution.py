from solution import accounts_merge


def _norm(rs):
    return sorted(tuple([r[0]] + sorted(r[1:])) for r in rs)


def test_basic():
    accs = [
        ["John", "johnsmith@x", "john00@y"],
        ["John", "johnnybravo@z"],
        ["John", "johnsmith@x", "john_newyork@w"],
        ["Mary", "mary@x"],
    ]
    expected = [
        ["John", "john00@y", "john_newyork@w", "johnsmith@x"],
        ["John", "johnnybravo@z"],
        ["Mary", "mary@x"],
    ]
    assert _norm(accounts_merge(accs)) == _norm(expected)
