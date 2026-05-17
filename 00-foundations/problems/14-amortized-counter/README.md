# 14. Amortized append counter  `[medium]`

Implement a `DynamicArray` with `push(x)` and `__len__` that doubles its backing capacity when full. Track and expose:

- `copies` — total elements copied across all resizes so far.
- `capacity` — current backing-array capacity.

After `n` pushes the total `copies` must satisfy `copies <= 2n - 1` (the geometric-sum bound). Tests will assert this.

This is the textbook example of amortized `Θ(1)` per push despite occasional `Θ(n)` resizes (CLRS § 17.4).

## Class signature

```python
class DynamicArray:
    def __init__(self, initial_capacity: int = 1) -> None: ...
    def push(self, x: int) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i: int) -> int: ...
    capacity: int
    copies: int
```

## Hint

<details>
<summary>Hint</summary>

Use a fixed-size list as the backing store (`[None] * capacity`). When `len == capacity`, allocate a new list of size `2*capacity`, copy the old contents (counting each copy), and replace.
</details>

## Why this matters in production

`list.append` in Python and `std::vector::push_back` in C++ are *exactly* this. Knowing the amortized analysis lets you size hot-path containers correctly (`list = [None] * n_expected` pre-allocates and avoids resize copies entirely).
