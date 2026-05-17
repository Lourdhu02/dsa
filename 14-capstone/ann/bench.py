"""Brute-force ground truth + recall@k utilities."""

from __future__ import annotations

import numpy as np

from .distance import batch_euclidean_sq


def brute_force_topk(query: np.ndarray, vectors: np.ndarray, k: int) -> list[int]:
    """Exact top-k by squared Euclidean.  Time: Θ(N · d).  Space: Θ(N)."""
    d = batch_euclidean_sq(query, vectors)
    return list(np.argsort(d)[:k])


def recall_at_k(predicted: list[int], truth: list[int]) -> float:
    """|predicted ∩ truth| / |truth|.  Both lists are sets of indices."""
    if not truth:
        return 1.0
    return len(set(predicted) & set(truth)) / len(truth)


def gen_clustered_vectors(n: int, d: int, n_clusters: int = 16, seed: int = 0) -> np.ndarray:
    """Generate ``n`` vectors in ``d`` dims clumped around ``n_clusters`` centers.

    More realistic than uniform random for evaluating ANN quality.
    """
    rng = np.random.default_rng(seed)
    centers = rng.normal(scale=5.0, size=(n_clusters, d)).astype(np.float32)
    assigns = rng.integers(0, n_clusters, size=n)
    noise = rng.normal(scale=1.0, size=(n, d)).astype(np.float32)
    return centers[assigns] + noise
