import numpy as np

from ann.distance import batch_euclidean_sq, cosine, euclidean_sq


def test_euclidean_sq_basic():
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, 6.0, 3.0])
    assert abs(euclidean_sq(a, b) - 25.0) < 1e-9


def test_cosine_basic():
    a = np.array([1.0, 0.0])
    b = np.array([0.0, 1.0])
    assert abs(cosine(a, b) - 1.0) < 1e-9
    assert abs(cosine(a, a) - 0.0) < 1e-6


def test_batch_matches_loop():
    rng = np.random.default_rng(0)
    q = rng.normal(size=(8,)).astype(np.float32)
    pts = rng.normal(size=(50, 8)).astype(np.float32)
    expected = np.array([euclidean_sq(q, p) for p in pts])
    got = batch_euclidean_sq(q, pts)
    assert np.allclose(expected, got, atol=1e-5)
