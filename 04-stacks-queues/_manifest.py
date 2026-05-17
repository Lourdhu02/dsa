"""Module 04 (stacks and queues) problem manifest."""

PROBLEMS = [
    {
        "slug": "01-valid-parentheses",
        "title": "Valid parentheses",
        "difficulty": "easy",
        "tags": ["stack"],
        "statement": "Given a string containing only `()[]{}`, return True iff every opener has a matching closer in the right order.",
        "signature": "def is_valid(s: str) -> bool: ...",
        "examples_md": """## Examples

| s | result |
|---|---|
| `"()"` | True |
| `"()[]{}"` | True |
| `"(]"` | False |
| `"([)]"` | False |""",
        "constraints": "",
        "hint": "Push openers onto a stack. On a closer, pop and check it matches.",
        "starter": """
def is_valid(s: str) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def is_valid(s: str) -> bool:
    \"\"\"Time: Θ(n).  Space: Θ(n).\"\"\"
    match = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in match.values():
            stack.append(ch)
        else:
            if not stack or stack.pop() != match[ch]:
                return False
    return not stack
""",
        "tests": """
import pytest

from solution import is_valid


@pytest.mark.parametrize(
    "s, expected",
    [("()", True), ("()[]{}", True), ("(]", False), ("([)]", False), ("", True), ("{[]}", True)],
)
def test_examples(s, expected):
    assert is_valid(s) is expected
""",
    },
    {
        "slug": "02-min-stack",
        "title": "Min stack",
        "difficulty": "easy",
        "tags": ["stack", "design"],
        "statement": "Design a stack supporting `push`, `pop`, `top`, and `get_min` — all in `Θ(1)`.",
        "signature": "class MinStack:\n    def push(self, x: int) -> None: ...\n    def pop(self) -> None: ...\n    def top(self) -> int: ...\n    def get_min(self) -> int: ...",
        "examples_md": """## Examples

```
ms = MinStack()
ms.push(-2); ms.push(0); ms.push(-3)
ms.get_min()   # -3
ms.pop()
ms.top()       # 0
ms.get_min()   # -2
```""",
        "constraints": "",
        "hint": "Maintain a parallel `min_stack` whose top is the min of everything in the main stack at that depth.",
        "starter": """
class MinStack:
    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def get_min(self) -> int:
        raise NotImplementedError
""",
        "reference": """
class MinStack:
    \"\"\"O(1) per op via paired min-stack.\"\"\"

    def __init__(self) -> None:
        self._data: list[int] = []
        self._mins: list[int] = []

    def push(self, x: int) -> None:
        self._data.append(x)
        if not self._mins or x <= self._mins[-1]:
            self._mins.append(x)

    def pop(self) -> None:
        x = self._data.pop()
        if x == self._mins[-1]:
            self._mins.pop()

    def top(self) -> int:
        return self._data[-1]

    def get_min(self) -> int:
        return self._mins[-1]
""",
        "tests": """
from solution import MinStack


def test_classic_flow():
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2


def test_repeated_min():
    ms = MinStack()
    ms.push(2)
    ms.push(2)
    ms.push(1)
    assert ms.get_min() == 1
    ms.pop()
    assert ms.get_min() == 2
    ms.pop()
    assert ms.get_min() == 2
""",
    },
    {
        "slug": "03-implement-queue-using-stacks",
        "title": "Implement queue using stacks",
        "difficulty": "easy",
        "tags": ["stack", "queue", "amortized"],
        "statement": "Implement a FIFO queue using only two stacks. Support `push`, `pop`, `peek`, `empty`. Amortized `Θ(1)` per op.",
        "signature": "class MyQueue:\n    def push(self, x: int) -> None: ...\n    def pop(self) -> int: ...\n    def peek(self) -> int: ...\n    def empty(self) -> bool: ...",
        "examples_md": """## Examples

```
q = MyQueue()
q.push(1); q.push(2); q.peek()  # 1
q.pop()                         # 1
q.empty()                       # False
```""",
        "constraints": "",
        "hint": "Two stacks: `in_stack` for pushes, `out_stack` for pops. When `out_stack` is empty, drain `in_stack` into it (reversing order).",
        "starter": """
class MyQueue:
    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def peek(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError
""",
        "reference": """
class MyQueue:
    \"\"\"Amortized O(1) per op: each element is pushed and popped on each stack at most once.\"\"\"

    def __init__(self) -> None:
        self._in: list[int] = []
        self._out: list[int] = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        self._shift()
        return self._out.pop()

    def peek(self) -> int:
        self._shift()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out

    def _shift(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
""",
        "tests": """
from solution import MyQueue


def test_classic_flow():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()
    assert q.pop() == 2
    assert q.empty()
""",
    },
    {
        "slug": "04-implement-stack-using-queues",
        "title": "Implement stack using queues",
        "difficulty": "easy",
        "tags": ["queue", "stack"],
        "statement": "Implement a LIFO stack using only a queue (`collections.deque` allowed for FIFO semantics). Support `push`, `pop`, `top`, `empty`.",
        "signature": "class MyStack:\n    def push(self, x: int) -> None: ...\n    def pop(self) -> int: ...\n    def top(self) -> int: ...\n    def empty(self) -> bool: ...",
        "examples_md": """## Examples

```
s = MyStack()
s.push(1); s.push(2); s.top()  # 2
s.pop()                         # 2
s.empty()                       # False
```""",
        "constraints": "",
        "hint": "After each push, rotate the queue so the just-added element is at the front. Then `pop` and `top` are constant-time on the queue front.",
        "starter": """
class MyStack:
    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError
""",
        "reference": """
from collections import deque


class MyStack:
    \"\"\"Rotate-on-push: push is Θ(n), pop/top are Θ(1).\"\"\"

    def __init__(self) -> None:
        self._q: deque[int] = deque()

    def push(self, x: int) -> None:
        self._q.append(x)
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self) -> int:
        return self._q.popleft()

    def top(self) -> int:
        return self._q[0]

    def empty(self) -> bool:
        return not self._q
""",
        "tests": """
from solution import MyStack


def test_classic_flow():
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert not s.empty()
    assert s.pop() == 1
    assert s.empty()
""",
    },
    {
        "slug": "05-next-greater-element",
        "title": "Next greater element",
        "difficulty": "medium",
        "tags": ["monotonic-stack"],
        "statement": "Given array `nums`, return an array where `out[i]` is the next strictly greater element of `nums` to the right of index `i`, or `-1` if none.",
        "signature": "def next_greater(nums: list[int]) -> list[int]: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[2, 1, 2, 4, 3]` | `[4, 2, 4, -1, -1]` |
| `[1, 2, 3, 4]` | `[2, 3, 4, -1]` |
| `[4, 3, 2, 1]` | `[-1, -1, -1, -1]` |""",
        "constraints": "",
        "hint": "Monotonic stack of indices, non-increasing from bottom to top.",
        "starter": """
def next_greater(nums: list[int]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def next_greater(nums: list[int]) -> list[int]:
    \"\"\"Time: Θ(n) amortized.  Space: Θ(n).\"\"\"
    n = len(nums)
    res = [-1] * n
    stack: list[int] = []
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res
""",
        "tests": """
import pytest

from solution import next_greater


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 1, 2, 4, 3], [4, 2, 4, -1, -1]),
        ([1, 2, 3, 4], [2, 3, 4, -1]),
        ([4, 3, 2, 1], [-1, -1, -1, -1]),
        ([], []),
        ([5], [-1]),
    ],
)
def test_examples(nums, expected):
    assert next_greater(nums) == expected
""",
    },
    {
        "slug": "06-daily-temperatures",
        "title": "Daily temperatures",
        "difficulty": "medium",
        "tags": ["monotonic-stack"],
        "statement": "Given an array `temps` of daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If no such day exists, `answer[i] = 0`.",
        "signature": "def daily_temperatures(temps: list[int]) -> list[int]: ...",
        "examples_md": """## Examples

| temps | answer |
|---|---|
| `[73, 74, 75, 71, 69, 72, 76, 73]` | `[1, 1, 4, 2, 1, 1, 0, 0]` |
| `[30, 40, 50, 60]` | `[1, 1, 1, 0]` |
| `[30, 60, 90]` | `[1, 1, 0]` |""",
        "constraints": "",
        "hint": "Same monotonic stack as next-greater, but record `i - stack.pop()` instead of the value.",
        "starter": """
def daily_temperatures(temps: list[int]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def daily_temperatures(temps: list[int]) -> list[int]:
    n = len(temps)
    res = [0] * n
    stack: list[int] = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res
""",
        "tests": """
import pytest

from solution import daily_temperatures


@pytest.mark.parametrize(
    "temps, expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80], [0, 0]),
    ],
)
def test_examples(temps, expected):
    assert daily_temperatures(temps) == expected
""",
    },
    {
        "slug": "07-evaluate-rpn",
        "title": "Evaluate Reverse Polish Notation",
        "difficulty": "medium",
        "tags": ["stack", "parsing"],
        "statement": "Evaluate an arithmetic expression in RPN (postfix). Tokens are integers or `+`, `-`, `*`, `/`. Integer division truncates toward zero.",
        "signature": "def eval_rpn(tokens: list[str]) -> int: ...",
        "examples_md": """## Examples

| tokens | result |
|---|---|
| `["2","1","+","3","*"]` | 9 |
| `["4","13","5","/","+"]` | 6 |
| `["10","6","9","3","+","-11","*","/","*","17","+","5","+"]` | 22 |""",
        "constraints": "",
        "hint": "Stack: push numbers; on an operator, pop two, apply, push the result. For division, use `int(a / b)` to truncate toward zero (NOT `a // b` which floors).",
        "starter": """
def eval_rpn(tokens: list[str]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def eval_rpn(tokens: list[str]) -> int:
    stack: list[int] = []
    for t in tokens:
        if t in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]
""",
        "tests": """
import pytest

from solution import eval_rpn


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["3"], 3),
    ],
)
def test_examples(tokens, expected):
    assert eval_rpn(tokens) == expected
""",
    },
    {
        "slug": "08-sliding-window-maximum",
        "title": "Sliding window maximum",
        "difficulty": "hard",
        "tags": ["monotonic-deque"],
        "statement": "Given array `nums` and integer `k`, return the maximum of each contiguous subarray of length `k`. Solve in `Θ(n)`.",
        "signature": "def max_sliding_window(nums: list[int], k: int) -> list[int]: ...",
        "examples_md": """## Examples

| nums | k | result |
|---|---|---|
| `[1,3,-1,-3,5,3,6,7]` | 3 | `[3,3,5,5,6,7]` |
| `[1]` | 1 | `[1]` |
| `[9,11]` | 2 | `[11]` |""",
        "constraints": "",
        "hint": "Monotonic deque of indices, strictly decreasing in value. On each step: pop back while smaller-or-equal to new value; append new index; pop front if out of window. Front is window max.",
        "starter": """
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    \"\"\"Time: Θ(n).  Space: Θ(k).\"\"\"
    if k <= 0:
        return []
    dq: deque[int] = deque()
    out: list[int] = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
""",
        "tests": """
import pytest

from solution import max_sliding_window


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
    ],
)
def test_examples(nums, k, expected):
    assert max_sliding_window(nums, k) == expected
""",
    },
    {
        "slug": "09-decode-string",
        "title": "Decode string",
        "difficulty": "medium",
        "tags": ["stack", "parsing"],
        "statement": "Given an encoded string like `3[a]2[bc]`, decode it to `\"aaabcbc\"`. Encoding rule: `k[encoded_string]` repeats `encoded_string` exactly `k` times. Brackets can nest.",
        "signature": "def decode_string(s: str) -> str: ...",
        "examples_md": """## Examples

| s | decoded |
|---|---|
| `"3[a]2[bc]"` | `"aaabcbc"` |
| `"3[a2[c]]"` | `"accaccacc"` |
| `"2[abc]3[cd]ef"` | `"abcabccdcdcdef"` |""",
        "constraints": "",
        "hint": "Two stacks: one for repeat counts, one for partially-built strings. On `[`, push the current count and current string; reset. On `]`, pop and combine.",
        "starter": """
def decode_string(s: str) -> str:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def decode_string(s: str) -> str:
    count_stack: list[int] = []
    str_stack: list[str] = []
    cur = ""
    k = 0
    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == "[":
            count_stack.append(k)
            str_stack.append(cur)
            k = 0
            cur = ""
        elif ch == "]":
            mult = count_stack.pop()
            prev = str_stack.pop()
            cur = prev + cur * mult
        else:
            cur += ch
    return cur
""",
        "tests": """
import pytest

from solution import decode_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc", "abc"),
        ("10[a]", "aaaaaaaaaa"),
    ],
)
def test_examples(s, expected):
    assert decode_string(s) == expected
""",
    },
    {
        "slug": "10-simplify-path",
        "title": "Simplify path",
        "difficulty": "medium",
        "tags": ["stack"],
        "statement": "Given a Unix-style absolute path, return its canonical form: collapse `.`, `..`, and consecutive slashes.",
        "signature": "def simplify_path(path: str) -> str: ...",
        "examples_md": """## Examples

| path | result |
|---|---|
| `"/home/"` | `"/home"` |
| `"/../"` | `"/"` |
| `"/home//foo/"` | `"/home/foo"` |
| `"/a/./b/../../c/"` | `"/c"` |""",
        "constraints": "",
        "hint": "Split by `/`. For each piece: skip empty/`.`, pop on `..`, push otherwise.",
        "starter": """
def simplify_path(path: str) -> str:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def simplify_path(path: str) -> str:
    stack: list[str] = []
    for piece in path.split("/"):
        if piece == "" or piece == ".":
            continue
        if piece == "..":
            if stack:
                stack.pop()
        else:
            stack.append(piece)
    return "/" + "/".join(stack)
""",
        "tests": """
import pytest

from solution import simplify_path


@pytest.mark.parametrize(
    "path, expected",
    [
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c"),
        ("/", "/"),
        ("/a//b////c/d//././/..", "/a/b/c"),
    ],
)
def test_examples(path, expected):
    assert simplify_path(path) == expected
""",
    },
    {
        "slug": "11-asteroid-collision",
        "title": "Asteroid collision",
        "difficulty": "medium",
        "tags": ["stack", "simulation"],
        "statement": "Given an array `asteroids` of nonzero integers where positive values move right and negative values move left at the same speed, simulate collisions. Two asteroids in collision: the smaller (by absolute value) explodes; equal-sized both explode. Return the final state.",
        "signature": "def asteroid_collision(asteroids: list[int]) -> list[int]: ...",
        "examples_md": """## Examples

| input | output |
|---|---|
| `[5, 10, -5]` | `[5, 10]` |
| `[8, -8]` | `[]` |
| `[10, 2, -5]` | `[10]` |
| `[-2, -1, 1, 2]` | `[-2, -1, 1, 2]` |""",
        "constraints": "",
        "hint": "Stack. Push each asteroid; if the top is positive and the new one is negative, resolve collisions until stable.",
        "starter": """
def asteroid_collision(asteroids: list[int]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def asteroid_collision(asteroids: list[int]) -> list[int]:
    stack: list[int] = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and stack and stack[-1] > 0:
            top = stack[-1]
            if top < -a:
                stack.pop()
                continue
            if top == -a:
                stack.pop()
            alive = False
        if alive:
            stack.append(a)
    return stack
""",
        "tests": """
import pytest

from solution import asteroid_collision


@pytest.mark.parametrize(
    "a, expected",
    [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        ([], []),
    ],
)
def test_examples(a, expected):
    assert asteroid_collision(a) == expected
""",
    },
    {
        "slug": "12-largest-rectangle-histogram",
        "title": "Largest rectangle in histogram",
        "difficulty": "hard",
        "tags": ["monotonic-stack"],
        "statement": "Given an array `heights` of bar heights (each width 1), return the area of the largest rectangle in the histogram.",
        "signature": "def largest_rectangle(heights: list[int]) -> int: ...",
        "examples_md": """## Examples

| heights | answer |
|---|---|
| `[2, 1, 5, 6, 2, 3]` | 10 |
| `[2, 4]` | 4 |
| `[1]` | 1 |""",
        "constraints": "",
        "hint": "Monotonic stack of bar indices, increasing in height. When a shorter bar arrives, pop and compute the rectangle that ends just before this bar with the popped bar as the smallest. Pad with a 0-height sentinel.",
        "starter": """
def largest_rectangle(heights: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def largest_rectangle(heights: list[int]) -> int:
    \"\"\"Time: Θ(n) amortized.  Space: Θ(n).\"\"\"
    heights = heights + [0]
    stack: list[int] = []
    best = 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = heights[top] * width
            if area > best:
                best = area
        stack.append(i)
    return best
""",
        "tests": """
import pytest

from solution import largest_rectangle


@pytest.mark.parametrize(
    "h, expected",
    [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([], 0),
        ([1, 1, 1, 1], 4),
        ([6, 7, 5, 2, 4, 5, 9, 3], 16),
    ],
)
def test_examples(h, expected):
    assert largest_rectangle(h) == expected
""",
    },
    {
        "slug": "13-trapping-rain-water-stack",
        "title": "Trapping rain water (monotonic stack)",
        "difficulty": "hard",
        "tags": ["monotonic-stack"],
        "statement": "Same problem as module 01 problem 15, but implement using a monotonic stack so you internalize the second canonical pattern.",
        "signature": "def trap(height: list[int]) -> int: ...",
        "examples_md": """## Examples

| height | trapped |
|---|---|
| `[0,1,0,2,1,0,1,3,2,1,2,1]` | 6 |
| `[4,2,0,3,2,5]` | 9 |""",
        "constraints": "",
        "hint": "Stack of indices in decreasing height. On a new bar that is taller than the top, pop the top, compute trapped water between the new top of the stack and the new bar, bounded by min of their heights.",
        "starter": """
def trap(height: list[int]) -> int:
    # TODO: monotonic-stack version.
    raise NotImplementedError
""",
        "reference": """
def trap(height: list[int]) -> int:
    \"\"\"Time: Θ(n).  Space: Θ(n).  Compare to module 01's two-pointer Θ(1) space version.\"\"\"
    stack: list[int] = []
    total = 0
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if not stack:
                break
            left = stack[-1]
            width = i - left - 1
            bounded = min(height[left], h) - height[bottom]
            total += width * bounded
        stack.append(i)
    return total
""",
        "tests": """
import pytest

from solution import trap


@pytest.mark.parametrize(
    "h, expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([3], 0),
    ],
)
def test_examples(h, expected):
    assert trap(h) == expected
""",
    },
    {
        "slug": "14-design-circular-queue",
        "title": "Design circular queue",
        "difficulty": "medium",
        "tags": ["queue", "design"],
        "statement": "Implement `MyCircularQueue` with fixed capacity, `Θ(1)` per op. Support `en_queue`, `de_queue`, `front`, `rear`, `is_empty`, `is_full`.",
        "signature": "class MyCircularQueue:\n    def __init__(self, k: int) -> None: ...\n    def en_queue(self, value: int) -> bool: ...\n    def de_queue(self) -> bool: ...\n    def front(self) -> int: ...\n    def rear(self) -> int: ...\n    def is_empty(self) -> bool: ...\n    def is_full(self) -> bool: ...",
        "examples_md": """## Examples

```
q = MyCircularQueue(3)
q.en_queue(1)      # True
q.en_queue(2)      # True
q.en_queue(3)      # True
q.en_queue(4)      # False (full)
q.rear()           # 3
q.is_full()        # True
q.de_queue()       # True
q.en_queue(4)      # True
q.rear()           # 4
```""",
        "constraints": "",
        "hint": "Fixed array, head and tail indices, size counter. Wrap with `% k`.",
        "starter": """
class MyCircularQueue:
    def __init__(self, k: int) -> None:
        raise NotImplementedError

    def en_queue(self, value: int) -> bool:
        raise NotImplementedError

    def de_queue(self) -> bool:
        raise NotImplementedError

    def front(self) -> int:
        raise NotImplementedError

    def rear(self) -> int:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError
""",
        "reference": """
class MyCircularQueue:
    def __init__(self, k: int) -> None:
        self._cap = k
        self._buf: list[int] = [0] * k
        self._head = 0
        self._size = 0

    def en_queue(self, value: int) -> bool:
        if self._size == self._cap:
            return False
        self._buf[(self._head + self._size) % self._cap] = value
        self._size += 1
        return True

    def de_queue(self) -> bool:
        if self._size == 0:
            return False
        self._head = (self._head + 1) % self._cap
        self._size -= 1
        return True

    def front(self) -> int:
        if self._size == 0:
            return -1
        return self._buf[self._head]

    def rear(self) -> int:
        if self._size == 0:
            return -1
        return self._buf[(self._head + self._size - 1) % self._cap]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._cap
""",
        "tests": """
from solution import MyCircularQueue


def test_classic_flow():
    q = MyCircularQueue(3)
    assert q.en_queue(1)
    assert q.en_queue(2)
    assert q.en_queue(3)
    assert not q.en_queue(4)
    assert q.rear() == 3
    assert q.is_full()
    assert q.de_queue()
    assert q.en_queue(4)
    assert q.rear() == 4


def test_empty_returns_minus_one():
    q = MyCircularQueue(2)
    assert q.front() == -1
    assert q.rear() == -1
""",
    },
    {
        "slug": "15-online-stock-span",
        "title": "Online stock span",
        "difficulty": "medium",
        "tags": ["monotonic-stack", "design"],
        "statement": "Design a `StockSpanner.next(price)` that returns the *span* of today's price: the number of consecutive days (including today) for which the price was less than or equal to today's. Amortized `Θ(1)` per call.",
        "signature": "class StockSpanner:\n    def next(self, price: int) -> int: ...",
        "examples_md": """## Examples

```
ss = StockSpanner()
ss.next(100)   # 1
ss.next(80)    # 1
ss.next(60)    # 1
ss.next(70)    # 2
ss.next(60)    # 1
ss.next(75)    # 4
ss.next(85)    # 6
```""",
        "constraints": "",
        "hint": "Stack of `(price, span)` pairs. On a new price, while the top's price is `<= new_price`, pop and add its span. Push `(price, accumulated_span)`. Each entry is pushed and popped at most once across the whole call sequence — amortized `Θ(1)`.",
        "starter": """
class StockSpanner:
    def __init__(self) -> None:
        raise NotImplementedError

    def next(self, price: int) -> int:
        raise NotImplementedError
""",
        "reference": """
class StockSpanner:
    def __init__(self) -> None:
        self._stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self._stack and self._stack[-1][0] <= price:
            span += self._stack.pop()[1]
        self._stack.append((price, span))
        return span
""",
        "tests": """
from solution import StockSpanner


def test_canonical_sequence():
    ss = StockSpanner()
    given = [100, 80, 60, 70, 60, 75, 85]
    expected = [1, 1, 1, 2, 1, 4, 6]
    assert [ss.next(p) for p in given] == expected
""",
    },
    {
        "slug": "16-basic-calculator",
        "title": "Basic calculator (parens, +, -)",
        "difficulty": "hard",
        "tags": ["stack", "parsing"],
        "statement": "Evaluate a simple arithmetic expression containing non-negative integers, `+`, `-`, parentheses, and whitespace. No `*` or `/`.",
        "signature": "def calculate(s: str) -> int: ...",
        "examples_md": """## Examples

| s | result |
|---|---|
| `"1 + 1"` | 2 |
| `" 2-1 + 2 "` | 3 |
| `"(1+(4+5+2)-3)+(6+8)"` | 23 |""",
        "constraints": "",
        "hint": "Single pass with one stack. Carry a running `result`, `sign` (+1 / -1) and a `number` accumulator. On `(`, push `result` and `sign`, reset. On `)`, finalize and multiply by the popped sign.",
        "starter": """
def calculate(s: str) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def calculate(s: str) -> int:
    result = 0
    number = 0
    sign = 1
    stack: list[int] = []  # holds (result_so_far, sign_at_open_paren) flat
    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch in "+-":
            result += sign * number
            number = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ")":
            result += sign * number
            number = 0
            result *= stack.pop()
            result += stack.pop()
    return result + sign * number
""",
        "tests": """
import pytest

from solution import calculate


@pytest.mark.parametrize(
    "s, expected",
    [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("0", 0),
        ("-(1+2)", -3),
    ],
)
def test_examples(s, expected):
    assert calculate(s) == expected
""",
    },
    {
        "slug": "17-car-fleet",
        "title": "Car fleet",
        "difficulty": "medium",
        "tags": ["stack", "sort"],
        "statement": "`n` cars at positions `position[i]` moving toward target `T` at speeds `speed[i]`. A faster car catches a slower one to form a *fleet* (same speed, moving as one). Return the number of fleets that arrive at the target.",
        "signature": "def car_fleet(target: int, position: list[int], speed: list[int]) -> int: ...",
        "examples_md": """## Examples

| target | position | speed | result |
|---|---|---|---|
| 12 | `[10,8,0,5,3]` | `[2,4,1,1,3]` | 3 |
| 10 | `[3]` | `[3]` | 1 |""",
        "constraints": "",
        "hint": "Sort cars by starting position descending. Iterate and use a stack of *arrival times*. A car forms its own fleet only if it arrives strictly later than the car in front; otherwise it merges.",
        "starter": """
def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    stack: list[float] = []
    for p, s in cars:
        t = (target - p) / s
        if not stack or t > stack[-1]:
            stack.append(t)
    return len(stack)
""",
        "tests": """
import pytest

from solution import car_fleet


@pytest.mark.parametrize(
    "target, pos, speed, expected",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (10, [3], [3], 1),
        (100, [0, 2, 4], [4, 2, 1], 1),
    ],
)
def test_examples(target, pos, speed, expected):
    assert car_fleet(target, pos, speed) == expected
""",
    },
    {
        "slug": "18-exclusive-time-functions",
        "title": "Exclusive time of functions",
        "difficulty": "medium",
        "tags": ["stack", "simulation"],
        "statement": "Given the start/end logs of function calls in a single-threaded program, return the exclusive time spent in each function (time spent inside the function not counting time inside nested calls).",
        "signature": "def exclusive_time(n: int, logs: list[str]) -> list[int]: ...",
        "examples_md": """## Examples

| n | logs | result |
|---|---|---|
| 2 | `[\"0:start:0\",\"1:start:2\",\"1:end:5\",\"0:end:6\"]` | `[3, 4]` |""",
        "constraints": "",
        "hint": "Stack of currently active function ids. On `start`, charge elapsed time to the function on top of stack, then push. On `end`, charge elapsed time to the function being popped.",
        "starter": """
def exclusive_time(n: int, logs: list[str]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def exclusive_time(n: int, logs: list[str]) -> list[int]:
    res = [0] * n
    stack: list[int] = []
    prev = 0
    for entry in logs:
        parts = entry.split(":")
        fid, kind, t = int(parts[0]), parts[1], int(parts[2])
        if kind == "start":
            if stack:
                res[stack[-1]] += t - prev
            stack.append(fid)
            prev = t
        else:  # end
            res[stack.pop()] += t - prev + 1
            prev = t + 1
    return res
""",
        "tests": """
import pytest

from solution import exclusive_time


@pytest.mark.parametrize(
    "n, logs, expected",
    [
        (2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"], [3, 4]),
        (1, ["0:start:0", "0:start:2", "0:end:5", "0:end:6"], [7]),
    ],
)
def test_examples(n, logs, expected):
    assert exclusive_time(n, logs) == expected
""",
    },
]
