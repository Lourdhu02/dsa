# 03. Accounts merge  `[medium]`

Given accounts `[name, email1, email2, ...]`, merge accounts that share any email. Return merged accounts with `[name, sorted_emails...]` in any order.

## Function signature

```python
def accounts_merge(accounts: list[list[str]]) -> list[list[str]]: ...
```

## Examples

```
[
  ["John", "johnsmith@x", "john00@y"],
  ["John", "johnnybravo@z"],
  ["John", "johnsmith@x", "john_newyork@w"],
  ["Mary", "mary@x"]
]
->
[
  ["John", "john00@y", "john_newyork@w", "johnsmith@x"],
  ["John", "johnnybravo@z"],
  ["Mary", "mary@x"]
]
```



## Hint

<details>
<summary>Hint</summary>

Union all emails per account. Map email -> account index. Group emails by their root.
</details>
