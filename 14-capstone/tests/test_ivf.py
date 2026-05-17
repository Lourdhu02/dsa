import numpy as np
import pytest

from ann.bench import brute_force_topk, gen_clustered_vectors, recall_at_k
from ann.ivf import IVF


@pytest.fixture(scope="module")
def small_corpus():
    return gen_clustered_vectors(n=1000, d=16, n_clusters=8, seed=1)


def test_ivf_basic_recall(small_corpus):
    idx = IVF(nlist=16, n_iter=10, seed=0)
    idx.fit(small_corpus)
    rng = np.random.default_rng(123)
    queries = rng.normal(scale=2.0, size=(30, 16)).astype(np.float32)
    recalls = []
    for q in queries:
        truth = brute_force_topk(q, small_corpus, k=10)
        pred = [nid for nid, _ in idx.query(q, k=10, nprobe=8)]
        recalls.append(recall_at_k(pred, truth))
    avg = float(np.mean(recalls))
    assert avg >= 0.6, f"recall too low: {avg:.3f}"


def test_ivf_recall_grows_with_nprobe(small_corpus):
    idx = IVF(nlist=16, n_iter=10, seed=0)
    idx.fit(small_corpus)
    rng = np.random.default_rng(42)
    queries = rng.normal(scale=2.0, size=(20, 16)).astype(np.float32)
    truths = [brute_force_topk(q, small_corpus, k=10) for q in queries]

    def avg_recall(nprobe):
        return float(
            np.mean(
                [
                    recall_at_k([nid for nid, _ in idx.query(q, k=10, nprobe=nprobe)], t)
                    for q, t in zip(queries, truths)
                ]
            )
        )

    r1 = avg_recall(1)
    r8 = avg_recall(8)
    assert r8 >= r1, f"nprobe=8 recall ({r8:.2f}) should be >= nprobe=1 recall ({r1:.2f})"


def test_ivf_requires_fit():
    idx = IVF(nlist=4, n_iter=5)
    with pytest.raises(RuntimeError):
        idx.query(np.zeros(4, dtype=np.float32), k=5, nprobe=1)
