# Module 13 — Greedy, Backtracking, Bit Manipulation

**By the end you can:**
1. Recognize when a greedy choice is provably correct (and when it's a tempting wrong answer).
2. Sketch the **exchange argument** for proving a greedy algorithm.
3. Apply the backtracking template for permutations, combinations, and constraint satisfaction (N-queens, sudoku).
4. Manipulate bits idiomatically: XOR tricks, low-bit isolation, popcount, bitmask DP setup.

**Time budget:** 30 min reading + 6 h lab.

---

## 1. When greedy works

Greedy makes the locally optimal choice at each step. It is correct when:

| Property | Why it matters |
|---|---|
| **Greedy choice property** | The locally optimal choice is part of *some* globally optimal solution. |
| **Optimal substructure** | After making the greedy choice the remaining problem is the same shape. |

**Exchange argument:** to prove a greedy algorithm correct, take any optimal solution and exchange one of its choices for the greedy one without decreasing the objective. If this can always be done, the greedy is optimal.

The danger: greedy that *looks* right but isn't (e.g., 0/1 knapsack — greedy by value/weight ratio is wrong; needs DP).

| Pattern | Example |
|---|---|
| Sort + scan | Activity selection, interval scheduling |
| Heap-based pick | Task scheduling, Huffman coding |
| Two-pointer / running aggregate | Gas station, jump game, partition labels |

## 2. Backtracking template

```python
def backtrack(state, choices, accept, output):
    if accept(state):
        output.append(snapshot(state))
        return
    for c in choices(state):
        if not feasible(state, c):
            continue
        apply(state, c)
        backtrack(state, choices, accept, output)
        undo(state, c)
```

Three knobs:
- **`feasible`** — prune impossible branches early. The big difference between brute force and tractable backtracking.
- **`accept`** — when do we record a solution.
- **`undo`** — every state mutation must be reversible.

For permutations / combinations / subsets the choices are "pick item i if not yet picked". For constraint problems (N-queens, sudoku), the choices are "place value v in slot s if it doesn't conflict".

## 3. Bit manipulation cheatsheet

| Operation | Idiom |
|---|---|
| Test bit `i` | `x & (1 << i)` |
| Set bit `i` | `x \|= 1 << i` |
| Clear bit `i` | `x &= ~(1 << i)` |
| Flip bit `i` | `x ^= 1 << i` |
| Lowest set bit | `x & -x` |
| Clear lowest set bit | `x & (x - 1)` |
| Count set bits | `x.bit_count()` (3.10+) or Brian Kernighan loop |
| Iterate subsets of mask | `s = mask; while s: ...; s = (s - 1) & mask` |
| `a == b`? | `a ^ b == 0` |
| Min of (a, b) without compare | `b ^ ((a ^ b) & -(a < b))` (rarely useful) |

The XOR identity is the workhorse: `a ^ a = 0`, `a ^ 0 = a`, XOR is associative+commutative. So XOR-ing all elements of `[1..n]` minus an array of `n-1` distinct elements from that range gives the missing one.

## How to use this module

1. Read.
2. Skim `solutions/`.
3. `pytest 13-greedy-backtracking-bits/tests -q` should be green.
4. Work through `problems/`.

## Run

```
pytest 13-greedy-backtracking-bits -q
```

## References

- CLRS § 16 (greedy), § 17 (amortized — relevant to many greedy proofs).
- Knuth, TAOCP Vol 4A § 7.1 (bitwise tricks).
- Tim Roughgarden, *Algorithms Illuminated* Vol 3, ch. 13 (greedy proofs).
