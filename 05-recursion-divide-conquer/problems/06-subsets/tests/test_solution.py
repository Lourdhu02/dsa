from solution import subsets


def test_three_elements():
    assert sorted(map(tuple, subsets([1, 2, 3]))) == sorted(
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    )


def test_empty():
    assert subsets([]) == [[]]
