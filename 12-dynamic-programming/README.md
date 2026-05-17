# Module 12 — Dynamic Programming

**By the end you can:**
1. Recognize when a problem is "DP-shaped": optimal substructure + overlapping subproblems.
2. Convert a recursive solution into a top-down memoized version, then to a bottom-up table, then to a space-optimized version.
3. Apply the classical 1D, 2D, knapsack, and bitmask DP templates.

**Time budget:** 45 min reading + 8–10 h lab.

---

## 1. The two requirements

Dynamic programming applies when:

| Requirement | What it means |
|---|---|
| **Optimal substructure** | The optimal solution contains optimal solutions to subproblems. |
| **Overlapping subproblems** | The recursion would solve the same subproblem many times. |

If the recursion's tree has unique subproblems at every node, plain recursion is enough — DP doesn't help. If it doesn't have optimal substructure (e.g., longest **simple** path in a general graph), DP doesn't apply at all.

## 2. Top-down vs bottom-up

| Style | Build via | Pros | Cons |
|---|---|---|---|
| Top-down (memoized) | recursion + cache | matches the natural problem statement; only computes reachable states | function-call overhead, recursion depth |
| Bottom-up (tabulation) | iterative table fill | tighter constants, no stack | requires you to figure out the topological order of states |

Both have the same time complexity. Pick whichever is easier to reason about; convert if you hit a stack-depth or constant-factor wall.

## 3. The four classical shapes

| Shape | State | Transition |
|---|---|---|
| 1D linear | `dp[i]` | from one or more earlier `dp[j], j < i` |
| 2D grid | `dp[i][j]` | from `dp[i-1][j]`, `dp[i][j-1]`, sometimes `dp[i-1][j-1]` |
| Knapsack | `dp[i][w]` (item, capacity) | take or skip |
| Bitmask DP | `dp[mask][...]` | enumerate which item/edge to add to the set |

```mermaid
flowchart LR
    R[recursion] -->|cache subproblems| M[top-down memoized]
    M -->|swap recursion for table| B[bottom-up table]
    B -->|drop dimension you don't need| O[space-optimized]
```

## 4. Knapsack reference

**0/1 knapsack** (each item once):

```
dp[w] = max value with capacity w
for each item (weight, value):
    for w from W downto weight:
        dp[w] = max(dp[w], dp[w - weight] + value)
```

The inner loop **must** go top-down so each item is considered only once.

**Unbounded knapsack** (unlimited copies): same but inner loop bottom-up.

## 5. Edit distance (Levenshtein)

Classic 2D DP, `Θ(nm)` time and space, can drop to `Θ(min(n, m))` space.

```
dp[i][j] = min ops to transform s[:i] -> t[:j]
         = 0                                       if i == 0 → j inserts
         = 0                                       if j == 0 → i deletes
         = dp[i-1][j-1]                            if s[i-1] == t[j-1]
         = 1 + min(dp[i-1][j],   # delete from s
                   dp[i][j-1],   # insert into s
                   dp[i-1][j-1]) # substitute
```

Reference: Levenshtein (1966).

## 6. LIS — `Θ(n log n)` via patience sorting

The DP-from-scratch is `Θ(n²)` (`dp[i] = 1 + max(dp[j] for j<i if a[j]<a[i])`). The patience-sorting trick uses `bisect` on a `tails` array to get `Θ(n log n)`. Subtle: `tails` is **not** the actual LIS, but its length equals the LIS length.

## 7. Bitmask DP

When the state involves "which subset of n items have we chosen?" with small `n` (≤ 20), encode the subset as a bitmask integer in `[0, 2^n)`. Total states: `2^n × ...`. TSP is the canonical example: `dp[mask][i]` = min cost to visit subset `mask` ending at city `i`.

## How to use this module

1. Read.
2. Skim `solutions/dp.py` (knapsack, LIS, edit distance).
3. `pytest 12-dynamic-programming/tests -q` should be green.
4. Open `notebook.ipynb` to see DP tables visualized.
5. Work through `problems/`.

## Run

```
pytest 12-dynamic-programming -q
```

## References

- CLRS § 14 (DP), § 15 (greedy comparison).
- Bellman, R. (1957), *Dynamic Programming.* (The original.)
- Levenshtein, V. I. (1966), *Binary codes capable of correcting deletions, insertions and reversals.*
