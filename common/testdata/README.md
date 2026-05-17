# Shared test fixtures

Small, version-controlled datasets used by multiple modules:

| File | Used by | Description |
|---|---|---|
| `words_small.txt` | 10 (tries), 14 (capstone) | 200 lowercase English words for trie / autocomplete tests |
| `graph_small.json` | 09 (graphs) | 10-node directed weighted graph used as the canonical Dijkstra example |
| `sorted_array.json` | 06 (binary search) | Pre-sorted integers used by search tests |

Larger or generated data goes in `_generated/` and is gitignored.
