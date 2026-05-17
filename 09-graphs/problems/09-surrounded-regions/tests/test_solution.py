from solution import solve


def test_basic():
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solve(board)
    assert board == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]


def test_no_change_when_open():
    board = [["O", "O"], ["O", "O"]]
    solve(board)
    assert board == [["O", "O"], ["O", "O"]]
