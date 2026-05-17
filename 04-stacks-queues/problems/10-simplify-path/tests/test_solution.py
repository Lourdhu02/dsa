import pytest

from solution import simplify_path


@pytest.mark.parametrize(
    "path, expected",
    [
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c"),
        ("/", "/"),
        ("/a//b////c/d//././/..", "/a/b/c"),
    ],
)
def test_examples(path, expected):
    assert simplify_path(path) == expected
