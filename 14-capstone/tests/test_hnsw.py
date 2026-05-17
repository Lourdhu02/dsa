import os
import tempfile

import numpy as np
import pytest

from ann.bench import brute_force_topk, gen_clustered_vectors, recall_at_k
from ann.hnsw import HNSW


@pytest.fixture(scope="module")
def small_corpus():
    return gen_clustered_vectors(n=500, d=16, n_clusters=8, seed=1)


def test_hnsw_returns_self_in_topk(small_corpus):
    idx = HNSW(dim=16, M=16, ef_construction=64, seed=0)
    for v in small_corpus:
        idx.add(v)
    # Query each vector; it must be its own closest neighbor.
    for i in range(0, 500, 50):
        results = idx.query(small_corpus[i], k=1)
        assert results[0][0] == i


def test_hnsw_recall_against_brute_force(small_corpus):
    idx = HNSW(dim=16, M=16, ef_construction=128, ef_search=128, seed=42)
    for v in small_corpus:
        idx.add(v)
    rng = np.random.default_rng(99)
    queries = rng.normal(scale=2.0, size=(50, 16)).astype(np.float32)
    recalls = []
    for q in queries:
        truth = brute_force_topk(q, small_corpus, k=10)
        pred = [nid for nid, _ in idx.query(q, k=10)]
        recalls.append(recall_at_k(pred, truth))
    avg = float(np.mean(recalls))
    assert avg >= 0.85, f"recall too low: {avg:.3f}"


def test_hnsw_persistence(small_corpus):
    idx = HNSW(dim=16, M=8, ef_construction=64, seed=7)
    for v in small_corpus[:100]:
        idx.add(v)
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "idx.pkl")
        idx.save(path)
        loaded = HNSW.load(path)
    q = small_corpus[5]
    a = idx.query(q, k=5)
    b = loaded.query(q, k=5)
    assert [x[0] for x in a] == [x[0] for x in b]


def test_invalid_input_dim():
    idx = HNSW(dim=4)
    with pytest.raises(ValueError):
        idx.add(np.zeros(8, dtype=np.float32))


def test_query_empty_index():
    idx = HNSW(dim=4)
    assert idx.query(np.zeros(4, dtype=np.float32), k=5) == []
