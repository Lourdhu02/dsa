"""IVF baseline: k-means centroids + inverted lists.

Time:
    train (N, d, K, iters): O(N · K · d · iters)
    query (nprobe):         O(K · d + (nprobe / K) · N · d)
Space: O(N + K · d).

This is the simplest form (no product quantization).  Hit the original Jegou,
Douze & Schmid (2011) paper for IVF+PQ.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .distance import batch_euclidean_sq


@dataclass
class IVF:
    nlist: int = 64
    n_iter: int = 20
    seed: int = 42

    def __post_init__(self) -> None:
        self._centroids: np.ndarray | None = None
        self._lists: list[list[int]] | None = None
        self._vectors: np.ndarray | None = None

    def fit(self, vectors: np.ndarray) -> None:
        """k-means on ``vectors`` (Lloyd's algorithm)."""
        rng = np.random.default_rng(self.seed)
        n = len(vectors)
        if n < self.nlist:
            raise ValueError("nlist must not exceed number of vectors")
        idx = rng.choice(n, size=self.nlist, replace=False)
        centroids = vectors[idx].astype(np.float32, copy=True)
        for _ in range(self.n_iter):
            assigns = self._assign(vectors, centroids)
            new_c = np.zeros_like(centroids)
            counts = np.zeros(self.nlist, dtype=np.int64)
            np.add.at(new_c, assigns, vectors)
            np.add.at(counts, assigns, 1)
            mask = counts > 0
            new_c[mask] /= counts[mask, None]
            # Keep dead centroids stable rather than blowing them up.
            new_c[~mask] = centroids[~mask]
            if np.allclose(new_c, centroids, atol=1e-6):
                centroids = new_c
                break
            centroids = new_c
        self._centroids = centroids
        self._vectors = vectors.astype(np.float32, copy=True)
        assigns = self._assign(self._vectors, centroids)
        self._lists = [[] for _ in range(self.nlist)]
        for i, c in enumerate(assigns):
            self._lists[int(c)].append(i)

    def query(self, q: np.ndarray, k: int = 10, nprobe: int = 4) -> list[tuple[int, float]]:
        if self._centroids is None or self._lists is None or self._vectors is None:
            raise RuntimeError("call .fit() first")
        q = q.astype(np.float32, copy=False)
        d_to_centroids = batch_euclidean_sq(q, self._centroids)
        probe_ids = np.argsort(d_to_centroids)[:nprobe]
        candidate_ids: list[int] = []
        for c in probe_ids:
            candidate_ids.extend(self._lists[int(c)])
        if not candidate_ids:
            return []
        cands = self._vectors[candidate_ids]
        d = batch_euclidean_sq(q, cands)
        order = np.argsort(d)[:k]
        return [(candidate_ids[int(i)], float(d[i])) for i in order]

    def _assign(self, vectors: np.ndarray, centroids: np.ndarray) -> np.ndarray:
        # ||x - c||^2 = ||x||^2 - 2 x.c + ||c||^2; constant ||x||^2 doesn't affect argmin.
        x_norm = np.einsum("ij,ij->i", vectors, vectors)[:, None]
        c_norm = np.einsum("ij,ij->i", centroids, centroids)[None, :]
        cross = vectors @ centroids.T
        d = x_norm - 2 * cross + c_norm
        return np.argmin(d, axis=1)
