from solution import permute


def test_three_elements():
    result = permute([1, 2, 3])
    assert sorted(map(tuple, result)) == sorted(
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    )


def test_empty():
    assert permute([]) == [[]]


def test_single():
    assert permute([7]) == [[7]]
