"""Minimal-but-real HNSW index.

This is an educational implementation: clear, hand-rolled, no Cython.  It is
~50-100x slower than ``hnswlib`` but exposes every algorithmic decision.

References:
    Malkov & Yashunin (2018), arXiv:1603.09320.
"""

from __future__ import annotations

import heapq
import math
import os
import pickle
import random
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from .distance import batch_euclidean_sq, euclidean_sq


@dataclass
class _NodeLevels:
    """Per-node neighbor lists, indexed by layer.  Layer 0 is the densest."""

    neighbors: list[list[int]] = field(default_factory=list)


class HNSW:
    """Hierarchical Navigable Small World index over float32 vectors.

    Hyperparameters
    ---------------
    M               : max neighbors per node per layer above 0 (layer 0 gets 2M).
    ef_construction : beam size during insertion.
    ef_search       : beam size during query (defaults to ef_construction).
    seed            : RNG seed for reproducible level assignment.

    Time complexity (typical, NOT worst case):
        build:   O(N log N · d)
        query:   O(log N · d)

    Worst case is O(N · d) when the small-world property fails.
    """

    def __init__(
        self,
        dim: int,
        M: int = 16,
        ef_construction: int = 200,
        ef_search: int | None = None,
        seed: int = 42,
    ) -> None:
        if M < 2:
            raise ValueError("M must be >= 2")
        self.dim = dim
        self.M = M
        self.M0 = 2 * M
        self.ef_construction = ef_construction
        self.ef_search = ef_search if ef_search is not None else ef_construction
        self._mL = 1.0 / math.log(M)
        self._rng = random.Random(seed)
        self._vectors: list[np.ndarray] = []
        self._levels: list[_NodeLevels] = []
        self._top_level: int = -1
        self._entry: int | None = None

    # ---- Public API --------------------------------------------------------

    def __len__(self) -> int:
        return len(self._vectors)

    def add(self, vector: np.ndarray) -> int:
        """Insert a single vector.  Returns its assigned id (= insertion order)."""
        v = self._as_vector(vector)
        node_id = len(self._vectors)
        level = self._sample_level()
        self._vectors.append(v)
        self._levels.append(_NodeLevels(neighbors=[[] for _ in range(level + 1)]))

        if self._entry is None:
            self._entry = node_id
            self._top_level = level
            return node_id

        # Phase 1: greedy descend from top down to level + 1.
        cur = self._entry
        for L in range(self._top_level, level, -1):
            cur = self._greedy_search_layer(v, cur, L)

        # Phase 2: from min(level, top_level) down to 0, gather neighbors and link.
        ep_set = {cur}
        for L in range(min(level, self._top_level), -1, -1):
            cands = self._search_layer(v, list(ep_set), self.ef_construction, L)
            M_at = self.M0 if L == 0 else self.M
            chosen = self._select_neighbors(v, cands, M_at)
            self._levels[node_id].neighbors[L] = chosen
            for nb in chosen:
                self._levels[nb].neighbors[L].append(node_id)
                if len(self._levels[nb].neighbors[L]) > M_at:
                    nb_vec = self._vectors[nb]
                    pruned = self._select_neighbors(nb_vec, self._levels[nb].neighbors[L], M_at)
                    self._levels[nb].neighbors[L] = pruned
            ep_set = set(cands[:1] if cands else [cur])

        if level > self._top_level:
            self._top_level = level
            self._entry = node_id
        return node_id

    def query(self, vector: np.ndarray, k: int = 10) -> list[tuple[int, float]]:
        """Return up to ``k`` nearest neighbors as ``[(id, distance²), ...]`` ascending."""
        if self._entry is None or k <= 0:
            return []
        v = self._as_vector(vector)
        cur = self._entry
        for L in range(self._top_level, 0, -1):
            cur = self._greedy_search_layer(v, cur, L)
        cands = self._search_layer(v, [cur], max(self.ef_search, k), 0)
        cands = cands[:k]
        return [(nid, euclidean_sq(v, self._vectors[nid])) for nid in cands]

    def save(self, path: str) -> None:
        """Persist the index to disk via pickle.

        For a real-world index use a tagged binary format and mmap; pickle is
        fine for this educational impl.
        """
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(
                {
                    "dim": self.dim,
                    "M": self.M,
                    "ef_construction": self.ef_construction,
                    "ef_search": self.ef_search,
                    "vectors": self._vectors,
                    "levels": self._levels,
                    "top_level": self._top_level,
                    "entry": self._entry,
                },
                f,
                protocol=pickle.HIGHEST_PROTOCOL,
            )

    @classmethod
    def load(cls, path: str) -> "HNSW":
        with open(path, "rb") as f:
            d = pickle.load(f)
        idx = cls(dim=d["dim"], M=d["M"], ef_construction=d["ef_construction"], ef_search=d["ef_search"])
        idx._vectors = d["vectors"]
        idx._levels = d["levels"]
        idx._top_level = d["top_level"]
        idx._entry = d["entry"]
        return idx

    # ---- Internals ---------------------------------------------------------

    def _as_vector(self, v: np.ndarray) -> np.ndarray:
        v = np.asarray(v, dtype=np.float32)
        if v.shape != (self.dim,):
            raise ValueError(f"expected shape ({self.dim},) got {v.shape}")
        return v

    def _sample_level(self) -> int:
        # Geometric distribution per the HNSW paper (Section 4.2.1).
        return int(-math.log(self._rng.random() + 1e-12) * self._mL)

    def _greedy_search_layer(self, q: np.ndarray, ep: int, layer: int) -> int:
        """Walk neighbors greedily towards q.  Returns the local minimum reached."""
        cur = ep
        cur_d = euclidean_sq(q, self._vectors[cur])
        improved = True
        while improved:
            improved = False
            for nb in self._levels[cur].neighbors[layer]:
                d = euclidean_sq(q, self._vectors[nb])
                if d < cur_d:
                    cur, cur_d = nb, d
                    improved = True
        return cur

    def _search_layer(self, q: np.ndarray, eps: list[int], ef: int, layer: int) -> list[int]:
        """Best-first search seeded from ``eps``.  Returns the ef closest ids."""
        visited: set[int] = set(eps)
        # candidates: min-heap by distance for the frontier
        candidates: list[tuple[float, int]] = []
        # results: max-heap by NEGATIVE distance so we can drop worst when over capacity
        results: list[tuple[float, int]] = []
        for ep in eps:
            d = euclidean_sq(q, self._vectors[ep])
            heapq.heappush(candidates, (d, ep))
            heapq.heappush(results, (-d, ep))
        while candidates:
            d, cur = heapq.heappop(candidates)
            worst_in_results = -results[0][0]
            if d > worst_in_results and len(results) >= ef:
                break
            for nb in self._levels[cur].neighbors[layer]:
                if nb in visited:
                    continue
                visited.add(nb)
                nd = euclidean_sq(q, self._vectors[nb])
                if len(results) < ef or nd < -results[0][0]:
                    heapq.heappush(candidates, (nd, nb))
                    heapq.heappush(results, (-nd, nb))
                    if len(results) > ef:
                        heapq.heappop(results)
        return [nid for _, nid in sorted(results, key=lambda x: -x[0])]

    def _select_neighbors(self, q: np.ndarray, candidates: list[int], M: int) -> list[int]:
        """Take the M closest candidates to q.

        The paper offers a more elaborate "select neighbors heuristic" that
        balances clustering vs spread; we keep it simple here.
        """
        if len(candidates) <= M:
            return list(candidates)
        if not candidates:
            return []
        pts = np.stack([self._vectors[c] for c in candidates])
        dists = batch_euclidean_sq(q, pts)
        order = np.argsort(dists)[:M]
        return [candidates[int(i)] for i in order]
