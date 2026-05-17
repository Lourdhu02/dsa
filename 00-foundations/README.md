# Module 00 — Foundations

**By the end you can:**
1. Install Python 3.11+ and `pytest` on Windows 11 and run one green test.
2. State the formal definitions of `O`, `Ω`, `Θ`, `o`, `ω` and use them without hand-waving.
3. Solve standard divide-and-conquer recurrences with the master theorem.
4. Distinguish worst, average, and amortized cost and explain when each matters in production.

**Time budget:** 60 min reading + 90 min lab (toolchain + first 6 problems).

---

## 1. Toolchain install (Windows 11 primary)

### 1.1 Install Python 3.11+

Pick one path:

**Option A — Microsoft Store (simplest):**

1. Open Microsoft Store, search "Python 3.12", install.
2. Confirm: `python --version` should print `Python 3.12.x`.

**Option B — Official installer (best for advanced users):**

1. Download from https://www.python.org/downloads/windows/.
2. **Check "Add python.exe to PATH"** during install.
3. Confirm: `py -3.12 --version`.

**macOS:** `brew install python@3.12`. **Linux (Ubuntu/Debian):** `sudo apt install python3.12 python3.12-venv`.

### 1.2 Create a virtual environment and install deps

From the repo root:

```powershell
# PowerShell on Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```bash
# bash on macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> **PowerShell execution policy:** if `Activate.ps1` fails, run once as Administrator: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.

### 1.3 Run one green test

```
pytest 00-foundations/tests -q
```

You should see something like:

```
....                                                                     [100%]
4 passed in 0.05s
```

If that's green, the loop works. Move on. If not, see `Troubleshooting` at the bottom of this file.

### 1.4 VS Code (optional but recommended)

```powershell
# install recommended extensions
Get-Content vscode/extensions.md  # read the list
# copy the example settings into a workspace settings file
Copy-Item vscode\settings.example.json .vscode\settings.json
```

Then `code .` from the repo root and VS Code will offer to run pytest in the gutter.

---

## 2. The RAM model

A claim like "binary search is O(log n)" is meaningless without a cost model. We use the **word RAM** model:

| Operation | Cost |
|---|---|
| Arithmetic on a Θ(log n)-bit word | Θ(1) |
| Array indexing | Θ(1) |
| Compare two words | Θ(1) |
| Memory allocation of k words | Θ(k) |

This is realistic for modern CPUs up to about 2^64 elements but it explicitly **ignores** the memory hierarchy (L1 / L2 / DRAM / disk). Two algorithms with the same `O(n log n)` time can differ 10× on a real machine because of cache locality.

When you need a cache-aware model, see Aggarwal & Vitter's external-memory model (cited in `resources/bibliography.md`).

## 3. Asymptotic notation — definitions

Let `f, g : ℕ → ℝ⁺`. CLRS § 3.2 gives:

| Notation | Definition |
|---|---|
| `f = O(g)` | ∃ c > 0, n₀ s.t. ∀n ≥ n₀: 0 ≤ f(n) ≤ c · g(n) |
| `f = Ω(g)` | ∃ c > 0, n₀ s.t. ∀n ≥ n₀: 0 ≤ c · g(n) ≤ f(n) |
| `f = Θ(g)` | f = O(g) **and** f = Ω(g) |
| `f = o(g)` | ∀ c > 0, ∃ n₀ s.t. ∀n ≥ n₀: 0 ≤ f(n) < c · g(n) |
| `f = ω(g)` | g = o(f) |

Two practical consequences engineers consistently miss:

1. **`O` is an upper bound, not a tight bound.** Saying "insertion sort is O(n³)" is technically true and useless. Prefer `Θ` when you can prove it. In casual interview language people use `O` to mean `Θ`; in code comments and lesson text we will use the precise letter.
2. **`O(n)` and `O(2n)` are the same set.** Constant factors and lower-order terms disappear in asymptotic notation, but they don't disappear in production. If your `O(n)` hot path has a 1000× constant you have a problem; the asymptotic class is hiding it.

## 4. Standard growth functions (smallest to largest)

```mermaid
graph LR
    A[1] --> B[log* n]
    B --> C[log log n]
    C --> D[log n]
    D --> E[sqrt n]
    E --> F[n]
    F --> G[n log n]
    G --> H[n^2]
    H --> I[n^3]
    I --> J[2^n]
    J --> K[n!]
```

Useful comparisons (CLRS § 3.3):

- For any constants `a > 0, b > 1`: `n^a = o(b^n)` — polynomials lose to exponentials.
- `log_b n = Θ(log n)` for any base `b > 1` — log base is irrelevant in Big-O.
- `Σ_{i=1}^n 1/i = Θ(log n)` — the harmonic sum (you'll meet this in quicksort and union-find proofs).

## 5. Recurrences and the master theorem

A divide-and-conquer recurrence has the form

```
T(n) = a · T(n/b) + f(n)
```

where `a ≥ 1` is the number of subproblems, `n/b` is the subproblem size, and `f(n)` is the per-level non-recursive cost (split + combine).

**Master theorem** (CLRS § 4.5):

| Case | Compare `f(n)` to `n^(log_b a)` | T(n) |
|---|---|---|
| 1 | `f = O(n^(log_b a − ε))` for some ε > 0 | `Θ(n^(log_b a))` |
| 2 | `f = Θ(n^(log_b a) · log^k n)`, k ≥ 0 | `Θ(n^(log_b a) · log^(k+1) n)` |
| 3 | `f = Ω(n^(log_b a + ε))` and a·f(n/b) ≤ c·f(n) for some c < 1 | `Θ(f(n))` |

Worked examples:

| Recurrence | a | b | n^(log_b a) | f(n) | Case | T(n) |
|---|---|---|---|---|---|---|
| `T(n) = 2T(n/2) + Θ(n)` (merge sort) | 2 | 2 | n | n | 2, k=0 | Θ(n log n) |
| `T(n) = T(n/2) + Θ(1)` (binary search) | 1 | 2 | 1 | 1 | 2, k=0 | Θ(log n) |
| `T(n) = 7T(n/2) + Θ(n²)` (Strassen) | 7 | 2 | n^(log₂ 7) ≈ n^2.807 | n² | 1 | Θ(n^log₂ 7) |
| `T(n) = 2T(n/2) + Θ(n²)` | 2 | 2 | n | n² | 3 | Θ(n²) |
| `T(n) = 4T(n/2) + Θ(n²)` | 4 | 2 | n² | n² | 2 | Θ(n² log n) |

**When the master theorem doesn't apply:** the recurrence isn't in standard form (e.g. `T(n) = T(n-1) + Θ(n)`), `f(n)` isn't polynomial, or the regularity condition in case 3 fails. Use the recursion-tree method or the substitution method (CLRS § 4.3-4.4).

## 6. Amortized analysis

Worst-case-per-operation can be pessimistic when an expensive op is rare. **Amortized cost** = total cost over a sequence of `n` operations, divided by `n`.

Three methods (CLRS § 17):

1. **Aggregate** — bound total cost of `n` ops, divide.
2. **Accounting** — charge cheap ops a credit that pays for future expensive ones.
3. **Potential** — define a potential function `Φ` on the data structure; amortized cost = actual cost + ΔΦ.

The canonical example: **dynamic array `push`** (`list.append` in Python, `vector::push_back` in C++). When capacity is full we copy `n` elements to a 2x-larger buffer — that's a Θ(n) op. But over `n` pushes, total copy cost is `n + n/2 + n/4 + ... = Θ(n)` (geometric sum), so each push is amortized Θ(1).

Crucially: amortized Θ(1) does **not** mean "almost always Θ(1)". One in every `log n` pushes is still Θ(n). If you can't tolerate latency spikes (real-time systems, GC-sensitive ML pipelines), reach for an amortized analysis with care.

## 7. Loop invariants

A loop invariant is a predicate that is true:
- **before** the loop starts,
- **after** every iteration (maintenance),
- and is strong enough at termination to prove correctness.

When you write a correctness comment on a non-trivial loop, write the invariant — it's the only thing that survives refactoring. Example for `max`:

```python
def find_max(xs: list[int]) -> int:
    # Invariant: best == max(xs[0:i+1]).
    best = xs[0]
    for i in range(1, len(xs)):
        if xs[i] > best:
            best = xs[i]
    # On exit i = len(xs)-1, so best == max(xs[0:len(xs)]) == max(xs).
    return best
```

We use invariants throughout the course. Module 04 (monotonic stacks) is where the discipline pays off the most.

---

## How to use this module

1. Read this README.
2. Skim `solutions/growth.py` and `solutions/recurrences.py` (the building blocks the lesson talks about, in code).
3. Run `pytest 00-foundations/tests -q`. It should be green.
4. Open `notebook.ipynb` to see growth curves rendered.
5. Work through `problems/` from `01-hello-pytest` upward. Each problem has a starter `solution.py` and tests; fill in the starter, run its tests, then peek at `reference.py` if stuck.

## Run the tests

| Scope | Command |
|---|---|
| All reference impls in this module | `pytest 00-foundations/tests -q` |
| One specific problem | `pytest 00-foundations/problems/03-power-fast/tests -q` |
| All problems in this module | `pytest 00-foundations/problems -q` |

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `pytest: command not found` | venv not activated | Activate `.\.venv\Scripts\Activate.ps1`. |
| `Activate.ps1 cannot be loaded` | PowerShell execution policy | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` (one-time). |
| `ModuleNotFoundError: solution` | running from the wrong cwd | Always invoke `pytest` from the repo root. |
| Tests collect but all skip | `python --version` < 3.11 | The course uses `match` and PEP 604 unions; install 3.11+. |

## References

- CLRS 4th ed., chapters 2 (analysis), 3 (asymptotics), 4 (recurrences), 17 (amortized).
- Python timing: PEP 564 — `time.perf_counter_ns`.
- Python list growth strategy: `Objects/listobject.c` in CPython, `list_resize`.
