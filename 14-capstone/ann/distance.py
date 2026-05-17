"""Distance helpers for the capstone.

We accept ``numpy.ndarray`` for speed but keep the interface tiny so the rest
of the code is portable.
"""

from __future__ import annotations

import numpy as np


def euclidean_sq(a: np.ndarray, b: np.ndarray) -> float:
    """Squared Euclidean distance.

    Squared on purpose: comparison is monotone in the squared form, so we
    skip the sqrt in hot paths.
    """
    diff = a - b
    return float(np.dot(diff, diff))


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine distance = 1 - cosine_similarity.  Returns in ``[0, 2]``."""
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    if na == 0.0 or nb == 0.0:
        return 1.0
    return 1.0 - float(np.dot(a, b) / (na * nb))


def batch_euclidean_sq(query: np.ndarray, points: np.ndarray) -> np.ndarray:
    """Vectorized squared Euclidean from a single query to every row of points.

    Time:  O(n · d).  Space: O(n).
    """
    diff = points - query
    return np.einsum("ij,ij->i", diff, diff)
