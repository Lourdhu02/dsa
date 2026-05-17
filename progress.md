# Practice Progress

Tick boxes as you go. The CLI helper `python -m common.practice next` reads this file to suggest the next unfinished problem.

Tags: `E` easy, `M` medium, `H` hard.

## 00 Foundations
See [`00-foundations/problems/`](00-foundations/problems/) for the 18 problems in this module.

## 01 Arrays and Strings
See [`01-arrays-strings/problems/`](01-arrays-strings/problems/) for the 18 problems in this module.

## 02 Hashing
See [`02-hashing/problems/`](02-hashing/problems/) for the 18 problems in this module.

## 03 Linked Lists
See [`03-linked-lists/problems/`](03-linked-lists/problems/) for the 18 problems in this module.

## 04 Stacks and Queues
See [`04-stacks-queues/problems/`](04-stacks-queues/problems/) for the 18 problems in this module.

## 05 Recursion and Divide & Conquer
See [`05-recursion-divide-conquer/problems/`](05-recursion-divide-conquer/problems/) for the 18 problems in this module.

## 06 Sorting and Searching
See [`06-sorting-searching/problems/`](06-sorting-searching/problems/) for the 18 problems in this module.

## 07 Trees
See [`07-trees/problems/`](07-trees/problems/) for the 18 problems in this module.

## 08 Heaps
See [`08-heaps-priority-queues/problems/`](08-heaps-priority-queues/problems/) for the 18 problems in this module.

## 09 Graphs
See [`09-graphs/problems/`](09-graphs/problems/) for the 18 problems in this module.

## 10 Tries and Strings
See [`10-tries-strings/problems/`](10-tries-strings/problems/) for the 18 problems in this module.

## 11 Union-Find and Advanced Trees
See [`11-union-find-advanced-trees/problems/`](11-union-find-advanced-trees/problems/) for the 18 problems in this module.

## 12 Dynamic Programming
See [`12-dynamic-programming/problems/`](12-dynamic-programming/problems/) for the 18 problems in this module.

## 13 Greedy, Backtracking, Bits
See [`13-greedy-backtracking-bits/problems/`](13-greedy-backtracking-bits/problems/) for the 18 problems in this module.

## 14 Capstone
See [`14-capstone/README.md`](14-capstone/README.md).

---

The CLI reads each module's `problems/index.json` to compute progress. Mark a problem done by running:

```
python -m common.practice done 03-linked-lists/04-reverse-list
```

Or simply by passing all its tests:

```
python -m common.practice sync
```
