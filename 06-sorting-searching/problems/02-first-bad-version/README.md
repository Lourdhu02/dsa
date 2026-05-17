# 02. First bad version  `[easy]`

You have `n` versions [1, n]. There exists a smallest version `k` such that all versions `>= k` are bad. Find `k` using as few `is_bad(v)` calls as possible. `is_bad` is supplied as an argument here (it is supplied by an API in the real LeetCode problem).

## Function signature

```python
def first_bad_version(n: int, is_bad: Callable[[int], bool]) -> int: ...
```

## Examples

```
n=5, is_bad: 4 and 5 are bad, others are good
result: 4
```



## Hint

<details>
<summary>Hint</summary>

Binary search for the smallest k with is_bad(k) True. Use the half-open invariant `[lo, hi)`.
</details>
