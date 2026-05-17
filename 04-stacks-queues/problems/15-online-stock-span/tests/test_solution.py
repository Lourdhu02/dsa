from solution import StockSpanner


def test_canonical_sequence():
    ss = StockSpanner()
    given = [100, 80, 60, 70, 60, 75, 85]
    expected = [1, 1, 1, 2, 1, 4, 6]
    assert [ss.next(p) for p in given] == expected
