"""Matplotlib helpers for the notebooks.  Kept tiny on purpose.

These helpers expect matplotlib to be installed.  They are *only* imported by
notebook cells; the test suite does not require matplotlib.
"""

from __future__ import annotations

from typing import Iterable, Mapping, Sequence


def plot_growth(
    sizes: Sequence[int],
    series: Mapping[str, Sequence[float]],
    *,
    title: str = "Growth curves",
    ylabel: str = "time (ms)",
    log: bool = True,
):
    """Plot one or more measurement series on a single axis.

    Parameters
    ----------
    sizes    : x-axis values (input sizes).
    series   : mapping ``{label: y-values}``.  Each y-array must match ``sizes``.
    log      : if True, both axes are log-scaled (the standard way to read
               growth orders visually: a straight line of slope k corresponds
               to ``Theta(n^k)``).

    Returns the matplotlib ``Figure`` so the caller can save or further style.
    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7, 4.5))
    for label, ys in series.items():
        ax.plot(sizes, ys, marker="o", label=label)
    ax.set_xlabel("n")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    if log:
        ax.set_xscale("log")
        ax.set_yscale("log")
    ax.grid(True, which="both", linestyle=":", linewidth=0.5)
    ax.legend()
    fig.tight_layout()
    return fig


def plot_dp_table(table: Sequence[Sequence[int]], *, title: str = "DP table"):
    """Heat-map a 2-D DP table.  Useful in module 12 for visualizing fills."""
    import matplotlib.pyplot as plt
    import numpy as np

    arr = np.asarray(table)
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(arr, aspect="auto", cmap="viridis")
    ax.set_title(title)
    ax.set_xlabel("j")
    ax.set_ylabel("i")
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            ax.text(j, i, str(arr[i, j]), ha="center", va="center", fontsize=8, color="white")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    return fig


def plot_graph(adj: Mapping[int, Iterable[int]], *, title: str = "Graph", directed: bool = False):
    """Lightweight graph drawer using matplotlib only (no networkx dep).

    Lays out nodes on a circle.  Fine for graphs up to ~30 nodes — past that
    you want a real layout engine (Kamada-Kawai etc.).
    """
    import math

    import matplotlib.pyplot as plt

    nodes = sorted(adj.keys())
    n = len(nodes)
    pos = {v: (math.cos(2 * math.pi * i / n), math.sin(2 * math.pi * i / n)) for i, v in enumerate(nodes)}

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title)
    for u, neighbors in adj.items():
        for v in neighbors:
            x0, y0 = pos[u]
            x1, y1 = pos[v]
            if directed:
                ax.annotate(
                    "",
                    xy=(x1, y1),
                    xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", lw=1, color="gray"),
                )
            else:
                ax.plot([x0, x1], [y0, y1], color="gray", lw=1)
    for v, (x, y) in pos.items():
        ax.scatter([x], [y], s=400, color="#1f77b4", zorder=3)
        ax.text(x, y, str(v), ha="center", va="center", color="white", zorder=4)
    fig.tight_layout()
    return fig
