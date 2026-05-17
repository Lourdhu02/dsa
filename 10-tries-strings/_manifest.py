"""Module 10 (tries & strings) manifest."""

PROBLEMS = [
    {
        "slug": "01-implement-trie",
        "title": "Implement Trie (prefix tree)",
        "difficulty": "medium",
        "tags": ["trie", "design"],
        "statement": "Implement `Trie` with `insert(word)`, `search(word) -> bool`, `startswith(prefix) -> bool`.",
        "signature": "class Trie:\n    def insert(self, word: str) -> None: ...\n    def search(self, word: str) -> bool: ...\n    def startswith(self, prefix: str) -> bool: ...",
        "examples_md": """## Examples

```
t = Trie()
t.insert(\"apple\")
t.search(\"apple\")    # True
t.search(\"app\")      # False
t.startswith(\"app\")  # True
t.insert(\"app\")
t.search(\"app\")      # True
```""",
        "constraints": "",
        "hint": "Dict-of-dicts; an `END` sentinel marks a complete word.",
        "starter": """
class Trie:
    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startswith(self, prefix: str) -> bool:
        raise NotImplementedError
""",
        "reference": """
class Trie:
    _END = "$"

    def __init__(self) -> None:
        self._root: dict = {}

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self._END] = True

    def _walk(self, s: str):
        node = self._root
        for ch in s:
            node = node.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and self._END in node

    def startswith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
""",
        "tests": """
from solution import Trie


def test_basic_flow():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.startswith("app") is True
    t.insert("app")
    assert t.search("app") is True
""",
    },
    {
        "slug": "02-add-and-search-words",
        "title": "Design add and search words",
        "difficulty": "medium",
        "tags": ["trie", "dfs"],
        "statement": "Implement `WordDictionary` with `add_word(word)` and `search(word) -> bool` where `word` may contain `'.'` matching any single letter.",
        "signature": "class WordDictionary:\n    def add_word(self, word: str) -> None: ...\n    def search(self, word: str) -> bool: ...",
        "examples_md": """## Examples

```
wd = WordDictionary()
wd.add_word(\"bad\")
wd.add_word(\"dad\")
wd.add_word(\"mad\")
wd.search(\"pad\")   # False
wd.search(\"bad\")   # True
wd.search(\".ad\")   # True
wd.search(\"b..\")   # True
```""",
        "constraints": "",
        "hint": "Trie. On `'.'`, recurse into all children of the current node.",
        "starter": """
class WordDictionary:
    def __init__(self) -> None:
        raise NotImplementedError

    def add_word(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError
""",
        "reference": """
class WordDictionary:
    _END = "$"

    def __init__(self) -> None:
        self._root: dict = {}

    def add_word(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self._END] = True

    def search(self, word: str) -> bool:
        def _dfs(node, i):
            if i == len(word):
                return self._END in node
            ch = word[i]
            if ch == ".":
                for k, child in node.items():
                    if k == self._END:
                        continue
                    if _dfs(child, i + 1):
                        return True
                return False
            child = node.get(ch)
            return False if child is None else _dfs(child, i + 1)

        return _dfs(self._root, 0)
""",
        "tests": """
from solution import WordDictionary


def test_basic():
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
""",
    },
    {
        "slug": "03-word-search-ii",
        "title": "Word search II (trie + DFS)",
        "difficulty": "hard",
        "tags": ["trie", "dfs", "grid"],
        "statement": "Given a 2D board of letters and a list of words, return all words from the list that can be formed by 4-directionally adjacent cells (each cell used at most once per word).",
        "signature": "def find_words(board: list[list[str]], words: list[str]) -> list[str]: ...",
        "examples_md": """## Examples

```
board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
words = [\"oath\",\"pea\",\"eat\",\"rain\"]
result = [\"oath\",\"eat\"]
```""",
        "constraints": "",
        "hint": "Build a trie of words. DFS each cell against the trie. Mark cells visited; remove leaf words from the trie as found to prune.",
        "starter": """
def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    END = "$"
    root: dict = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node[END] = w

    found: list[str] = []
    m, n = len(board), len(board[0]) if board else 0

    def _dfs(i, j, node):
        ch = board[i][j]
        nxt = node.get(ch)
        if nxt is None:
            return
        word = nxt.pop(END, None)
        if word is not None:
            found.append(word)
        board[i][j] = "#"
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                _dfs(ni, nj, nxt)
        board[i][j] = ch
        if not nxt:
            node.pop(ch, None)

    for i in range(m):
        for j in range(n):
            _dfs(i, j, root)
    return found
""",
        "tests": """
from solution import find_words


def test_basic():
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
    words = ["oath", "pea", "eat", "rain"]
    assert sorted(find_words([row[:] for row in board], words)) == sorted(["oath", "eat"])


def test_empty_board():
    assert find_words([], ["a"]) == []
""",
    },
    {
        "slug": "04-longest-common-prefix",
        "title": "Longest common prefix",
        "difficulty": "easy",
        "tags": ["string", "trie-or-iterate"],
        "statement": "Return the longest common prefix among an array of strings; `\"\"` if none.",
        "signature": "def longest_common_prefix(strs: list[str]) -> str: ...",
        "examples_md": """## Examples

| strs | result |
|---|---|
| `[\"flower\",\"flow\",\"flight\"]` | `\"fl\"` |
| `[\"dog\",\"racecar\",\"car\"]` | `\"\"` |""",
        "constraints": "",
        "hint": "Compare characters of all strings at each position until mismatch.",
        "starter": """
def longest_common_prefix(strs: list[str]) -> str:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    for i, ch in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != ch:
                return strs[0][:i]
    return strs[0]
""",
        "tests": """
import pytest
from solution import longest_common_prefix


@pytest.mark.parametrize(
    "strs, expected",
    [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""), ([""], ""), (["a"], "a")],
)
def test_examples(strs, expected):
    assert longest_common_prefix(strs) == expected
""",
    },
    {
        "slug": "05-replace-words",
        "title": "Replace words (with shortest root)",
        "difficulty": "medium",
        "tags": ["trie"],
        "statement": "Given a `dictionary` of word roots and a `sentence`, replace every word in the sentence with its shortest root (if any). Words separated by single spaces.",
        "signature": "def replace_words(dictionary: list[str], sentence: str) -> str: ...",
        "examples_md": """## Examples

```
dictionary=[\"cat\",\"bat\",\"rat\"]
sentence=\"the cattle was rattled by the battery\"
result=\"the cat was rat by the bat\"
```""",
        "constraints": "",
        "hint": "Build a trie of roots; for each word, walk through it; emit the first complete-root path encountered.",
        "starter": """
def replace_words(dictionary: list[str], sentence: str) -> str:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def replace_words(dictionary: list[str], sentence: str) -> str:
    END = "$"
    root: dict = {}
    for w in dictionary:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node[END] = True

    def _shortest_root(word: str) -> str:
        node = root
        for i, ch in enumerate(word):
            if ch not in node:
                return word
            node = node[ch]
            if END in node:
                return word[: i + 1]
        return word

    return " ".join(_shortest_root(w) for w in sentence.split())
""",
        "tests": """
from solution import replace_words


def test_basic():
    assert replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"


def test_no_change():
    assert replace_words(["abc"], "hello world") == "hello world"
""",
    },
    {
        "slug": "06-strstr-needle-in-haystack",
        "title": "Implement strStr (needle in haystack)",
        "difficulty": "medium",
        "tags": ["kmp", "string-matching"],
        "statement": "Given two strings, return the index of the first occurrence of `needle` in `haystack`, or -1.",
        "signature": "def str_str(haystack: str, needle: str) -> int: ...",
        "examples_md": """## Examples

| haystack | needle | result |
|---|---|---|
| `\"sadbutsad\"` | `\"sad\"` | 0 |
| `\"leetcode\"` | `\"leeto\"` | -1 |""",
        "constraints": "",
        "hint": "KMP gives Θ(n+m). For interview: a Θ(n*m) naive scan is also accepted.",
        "starter": """
def str_str(haystack: str, needle: str) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    f = [0] * len(needle)
    k = 0
    for i in range(1, len(needle)):
        while k and needle[k] != needle[i]:
            k = f[k - 1]
        if needle[k] == needle[i]:
            k += 1
        f[i] = k
    k = 0
    for i, ch in enumerate(haystack):
        while k and needle[k] != ch:
            k = f[k - 1]
        if needle[k] == ch:
            k += 1
        if k == len(needle):
            return i - len(needle) + 1
    return -1
""",
        "tests": """
import pytest
from solution import str_str


@pytest.mark.parametrize(
    "h, n, expected",
    [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1), ("abc", "", 0), ("a", "a", 0)],
)
def test_examples(h, n, expected):
    assert str_str(h, n) == expected
""",
    },
    {
        "slug": "07-shortest-palindrome",
        "title": "Shortest palindrome",
        "difficulty": "hard",
        "tags": ["kmp"],
        "statement": "Return the shortest palindrome you can form by adding characters to the front of `s`.",
        "signature": "def shortest_palindrome(s: str) -> str: ...",
        "examples_md": """## Examples

| s | result |
|---|---|
| `\"aacecaaa\"` | `\"aaacecaaa\"` |
| `\"abcd\"` | `\"dcbabcd\"` |""",
        "constraints": "",
        "hint": "Find the longest palindromic prefix. Use KMP failure on `s + '#' + reverse(s)`.",
        "starter": """
def shortest_palindrome(s: str) -> str:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def shortest_palindrome(s: str) -> str:
    combined = s + "#" + s[::-1]
    f = [0] * len(combined)
    k = 0
    for i in range(1, len(combined)):
        while k and combined[k] != combined[i]:
            k = f[k - 1]
        if combined[k] == combined[i]:
            k += 1
        f[i] = k
    longest_pal_prefix = f[-1]
    return s[longest_pal_prefix:][::-1] + s
""",
        "tests": """
import pytest
from solution import shortest_palindrome


@pytest.mark.parametrize(
    "s, expected", [("aacecaaa", "aaacecaaa"), ("abcd", "dcbabcd"), ("", ""), ("a", "a")]
)
def test_examples(s, expected):
    assert shortest_palindrome(s) == expected
""",
    },
    {
        "slug": "08-z-algorithm-find-pattern",
        "title": "Pattern matching with Z-algorithm",
        "difficulty": "medium",
        "tags": ["z-algorithm"],
        "statement": "Implement Z-algorithm-based pattern search: return all starting indices of `pat` in `text`.",
        "signature": "def z_find(text: str, pat: str) -> list[int]: ...",
        "examples_md": """## Examples

| text | pat | result |
|---|---|---|
| `\"aaaaa\"` | `\"aa\"` | `[0, 1, 2, 3]` |
| `\"abracadabra\"` | `\"abra\"` | `[0, 7]` |""",
        "constraints": "",
        "hint": "Compute Z over `pat + '$' + text`; positions where Z == len(pat) are matches (offset by len(pat)+1).",
        "starter": """
def z_find(text: str, pat: str) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def z_function(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def z_find(text: str, pat: str) -> list[int]:
    if not pat:
        return list(range(len(text) + 1))
    combined = pat + "$" + text
    z = z_function(combined)
    out: list[int] = []
    m = len(pat)
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            out.append(i - m - 1)
    return out
""",
        "tests": """
import pytest
from solution import z_find


@pytest.mark.parametrize(
    "text, pat, expected",
    [
        ("aaaaa", "aa", [0, 1, 2, 3]),
        ("abracadabra", "abra", [0, 7]),
        ("abc", "d", []),
    ],
)
def test_examples(text, pat, expected):
    assert z_find(text, pat) == expected
""",
    },
    {
        "slug": "09-rabin-karp",
        "title": "Pattern search with Rabin-Karp",
        "difficulty": "medium",
        "tags": ["rabin-karp", "rolling-hash"],
        "statement": "Implement Rabin-Karp pattern matching: return all starting indices of `pat` in `text`.",
        "signature": "def rabin_karp(text: str, pat: str) -> list[int]: ...",
        "examples_md": """## Examples

| text | pat | result |
|---|---|---|
| `\"abracadabra\"` | `\"abra\"` | `[0, 7]` |""",
        "constraints": "",
        "hint": "Polynomial rolling hash mod a large prime; verify each hash hit with character compare to defeat collisions.",
        "starter": """
def rabin_karp(text: str, pat: str) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def rabin_karp(text: str, pat: str) -> list[int]:
    n, m = len(text), len(pat)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    BASE, MOD = 257, (1 << 61) - 1
    pat_h = 0
    win_h = 0
    high = pow(BASE, m - 1, MOD)
    for i in range(m):
        pat_h = (pat_h * BASE + ord(pat[i])) % MOD
        win_h = (win_h * BASE + ord(text[i])) % MOD
    out: list[int] = []
    for i in range(n - m + 1):
        if win_h == pat_h and text[i : i + m] == pat:
            out.append(i)
        if i + m < n:
            win_h = ((win_h - ord(text[i]) * high) * BASE + ord(text[i + m])) % MOD
    return out
""",
        "tests": """
import pytest
from solution import rabin_karp


@pytest.mark.parametrize(
    "text, pat, expected",
    [
        ("abracadabra", "abra", [0, 7]),
        ("aaaa", "aa", [0, 1, 2]),
        ("abc", "d", []),
        ("abc", "", [0, 1, 2, 3]),
    ],
)
def test_examples(text, pat, expected):
    assert rabin_karp(text, pat) == expected
""",
    },
    {
        "slug": "10-repeated-substring-pattern",
        "title": "Repeated substring pattern",
        "difficulty": "easy",
        "tags": ["string", "kmp-trick"],
        "statement": "Return True if `s` can be constructed by concatenating multiple copies of a non-empty proper substring.",
        "signature": "def repeated_substring_pattern(s: str) -> bool: ...",
        "examples_md": """## Examples

| s | result |
|---|---|
| `\"abab\"` | True |
| `\"aba\"` | False |
| `\"abcabcabcabc\"` | True |""",
        "constraints": "",
        "hint": "Trick: `(s + s)[1:-1]` contains `s` iff `s` is repeated.",
        "starter": """
def repeated_substring_pattern(s: str) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def repeated_substring_pattern(s: str) -> bool:
    return s in (s + s)[1:-1]
""",
        "tests": """
import pytest
from solution import repeated_substring_pattern


@pytest.mark.parametrize(
    "s, expected",
    [("abab", True), ("aba", False), ("abcabcabcabc", True), ("", False), ("a", False)],
)
def test_examples(s, expected):
    assert repeated_substring_pattern(s) is expected
""",
    },
    {
        "slug": "11-find-all-concatenated-words",
        "title": "Find all concatenated words",
        "difficulty": "hard",
        "tags": ["trie", "dp"],
        "statement": "Given a list of distinct words, return all words that are concatenations of at least TWO other words from the list.",
        "signature": "def find_all_concatenated_words(words: list[str]) -> list[str]: ...",
        "examples_md": """## Examples

```
words=[\"cat\",\"cats\",\"catsdogcats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\"]
result=[\"catsdogcats\",\"dogcatsdog\",\"ratcatdogcat\"]
```""",
        "constraints": "",
        "hint": "DP per word: `can[i]` = True iff `word[:i]` is a concatenation of at least k words. Use a set of all words.",
        "starter": """
def find_all_concatenated_words(words: list[str]) -> list[str]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_all_concatenated_words(words: list[str]) -> list[str]:
    word_set = set(words)
    out: list[str] = []

    def _can_concat(word: str) -> bool:
        if not word:
            return False
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and word[j:i] in word_set and not (j == 0 and i == n):
                    dp[i] = True
                    break
        return dp[n]

    for w in words:
        if _can_concat(w):
            out.append(w)
    return out
""",
        "tests": """
from solution import find_all_concatenated_words


def test_basic():
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    assert sorted(find_all_concatenated_words(words)) == sorted(["catsdogcats", "dogcatsdog", "ratcatdogcat"])


def test_no_concat():
    assert find_all_concatenated_words(["a", "b", "c"]) == []
""",
    },
    {
        "slug": "12-word-break-trie",
        "title": "Word break (trie + DP)",
        "difficulty": "medium",
        "tags": ["dp", "trie"],
        "statement": "Given a string `s` and a dictionary `word_dict`, return True if `s` can be segmented into a space-separated sequence of dictionary words.",
        "signature": "def word_break(s: str, word_dict: list[str]) -> bool: ...",
        "examples_md": """## Examples

| s | word_dict | result |
|---|---|---|
| `\"leetcode\"` | `[\"leet\",\"code\"]` | True |
| `\"applepenapple\"` | `[\"apple\",\"pen\"]` | True |
| `\"catsandog\"` | `[\"cats\",\"dog\",\"sand\",\"and\",\"cat\"]` | False |""",
        "constraints": "",
        "hint": "DP: `dp[i]` = True if `s[:i]` is segmentable. Walk the suffix dictionary at each position via a trie or set.",
        "starter": """
def word_break(s: str, word_dict: list[str]) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
""",
        "tests": """
import pytest
from solution import word_break


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ],
)
def test_examples(s, words, expected):
    assert word_break(s, words) is expected
""",
    },
    {
        "slug": "13-stream-of-characters",
        "title": "Stream of characters",
        "difficulty": "hard",
        "tags": ["trie", "design"],
        "statement": "Implement `StreamChecker(words)` and `query(letter) -> bool`. After each `query`, return True if the suffix of the stream matches any word in `words`.",
        "signature": "class StreamChecker:\n    def __init__(self, words: list[str]) -> None: ...\n    def query(self, letter: str) -> bool: ...",
        "examples_md": """## Examples

```
sc = StreamChecker([\"cd\",\"f\",\"kl\"])
sc.query(\"a\") -> False\nsc.query(\"b\") -> False\nsc.query(\"c\") -> False\nsc.query(\"d\") -> True\n
```""",
        "constraints": "",
        "hint": "Build a trie of REVERSED words. Maintain the stream in reverse (or just iterate the suffix backward) walking the trie until a word-end or mismatch.",
        "starter": """
class StreamChecker:
    def __init__(self, words: list[str]) -> None:
        raise NotImplementedError

    def query(self, letter: str) -> bool:
        raise NotImplementedError
""",
        "reference": """
class StreamChecker:
    _END = "$"

    def __init__(self, words: list[str]) -> None:
        self._root: dict = {}
        for w in words:
            node = self._root
            for ch in reversed(w):
                node = node.setdefault(ch, {})
            node[self._END] = True
        self._stream: list[str] = []

    def query(self, letter: str) -> bool:
        self._stream.append(letter)
        node = self._root
        for ch in reversed(self._stream):
            child = node.get(ch)
            if child is None:
                return False
            if self._END in child:
                return True
            node = child
        return False
""",
        "tests": """
from solution import StreamChecker


def test_basic_sequence():
    sc = StreamChecker(["cd", "f", "kl"])
    assert sc.query("a") is False
    assert sc.query("b") is False
    assert sc.query("c") is False
    assert sc.query("d") is True
    assert sc.query("e") is False
    assert sc.query("f") is True
""",
    },
    {
        "slug": "14-minimum-genetic-mutation",
        "title": "Minimum genetic mutation",
        "difficulty": "medium",
        "tags": ["bfs", "string"],
        "statement": "Given `start_gene`, `end_gene`, and a `bank` of valid genes (8-character strings of A,C,G,T), return the minimum number of single-character mutations to go from start to end through bank-only intermediates. -1 if impossible.",
        "signature": "def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int: ...",
        "examples_md": """## Examples

| start | end | bank | result |
|---|---|---|---|
| `\"AACCGGTT\"` | `\"AACCGGTA\"` | `[\"AACCGGTA\"]` | 1 |
| `\"AACCGGTT\"` | `\"AAACGGTA\"` | `[\"AACCGGTA\",\"AACCGCTA\",\"AAACGGTA\"]` | 2 |""",
        "constraints": "",
        "hint": "Treat each gene as a node, edges between bank genes that differ by one char. BFS.",
        "starter": """
def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import deque


def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int:
    bank_set = set(bank)
    if end_gene not in bank_set:
        return -1
    seen = {start_gene}
    q = deque([(start_gene, 0)])
    while q:
        gene, d = q.popleft()
        if gene == end_gene:
            return d
        for i in range(len(gene)):
            for ch in "ACGT":
                if ch == gene[i]:
                    continue
                nxt = gene[:i] + ch + gene[i + 1:]
                if nxt in bank_set and nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, d + 1))
    return -1
""",
        "tests": """
import pytest
from solution import min_mutation


@pytest.mark.parametrize(
    "s, e, bank, expected",
    [
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
        ("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3),
    ],
)
def test_examples(s, e, bank, expected):
    assert min_mutation(s, e, bank) == expected
""",
    },
    {
        "slug": "15-maximum-xor-of-two-numbers",
        "title": "Maximum XOR of two numbers (binary trie)",
        "difficulty": "medium",
        "tags": ["trie", "bit-manipulation"],
        "statement": "Given a list of non-negative integers, return the max XOR of any two of them. Solve in `Θ(n · 32)`.",
        "signature": "def find_maximum_xor(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[3, 10, 5, 25, 2, 8]` | 28 |
| `[0]` | 0 |""",
        "constraints": "",
        "hint": "Bitwise trie of the 32-bit representations. For each number, walk the trie greedily picking opposite bits to maximize XOR.",
        "starter": """
def find_maximum_xor(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_maximum_xor(nums: list[int]) -> int:
    BITS = 31  # safe for non-negative ints up to 2^31 - 1
    root: dict = {}
    for x in nums:
        node = root
        for i in range(BITS, -1, -1):
            b = (x >> i) & 1
            node = node.setdefault(b, {})
    best = 0
    for x in nums:
        node = root
        cur = 0
        for i in range(BITS, -1, -1):
            b = (x >> i) & 1
            target = 1 - b
            if target in node:
                cur |= (1 << i)
                node = node[target]
            else:
                node = node[b]
        best = max(best, cur)
    return best
""",
        "tests": """
import pytest
from solution import find_maximum_xor


@pytest.mark.parametrize(
    "nums, expected",
    [([3, 10, 5, 25, 2, 8], 28), ([0], 0), ([1, 2], 3), ([8, 10, 2], 10)],
)
def test_examples(nums, expected):
    assert find_maximum_xor(nums) == expected
""",
    },
    {
        "slug": "16-suffix-array-naive",
        "title": "Suffix array (naive build)",
        "difficulty": "medium",
        "tags": ["suffix-array", "string"],
        "statement": "Given a string `s`, return its suffix array — the indices `[i_0, i_1, ...]` such that `s[i_0:], s[i_1:], ...` is lexicographically sorted. Naive `Θ(n^2 log n)` is fine for the test sizes.",
        "signature": "def suffix_array(s: str) -> list[int]: ...",
        "examples_md": """## Examples

| s | result |
|---|---|
| `\"banana\"` | `[5, 3, 1, 0, 4, 2]` |
| `\"abc\"` | `[0, 1, 2]` |""",
        "constraints": "",
        "hint": "Just `sorted(range(len(s)), key=lambda i: s[i:])`. Real-world implementations use SA-IS or DC3 in `Θ(n)`; we don't here.",
        "starter": """
def suffix_array(s: str) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def suffix_array(s: str) -> list[int]:
    return sorted(range(len(s)), key=lambda i: s[i:])
""",
        "tests": """
import pytest
from solution import suffix_array


@pytest.mark.parametrize(
    "s, expected",
    [("banana", [5, 3, 1, 0, 4, 2]), ("abc", [0, 1, 2]), ("", [])],
)
def test_examples(s, expected):
    assert suffix_array(s) == expected
""",
    },
    {
        "slug": "17-autocomplete-system",
        "title": "Search autocomplete system",
        "difficulty": "hard",
        "tags": ["trie", "design", "heap"],
        "statement": "Design `AutocompleteSystem(sentences, times)` and `input(c) -> list[str]`. After each character, return the top 3 matching historical sentences (by frequency desc, then lex asc) for the prefix typed so far. Input `c == '#'` ends a sentence and adds it to history.",
        "signature": "class AutocompleteSystem:\n    def __init__(self, sentences: list[str], times: list[int]) -> None: ...\n    def input(self, c: str) -> list[str]: ...",
        "examples_md": """## Examples

```
ac = AutocompleteSystem([\"i love you\",\"island\",\"ironman\",\"i love leetcode\"], [5,3,2,2])
ac.input('i') -> [\"i love you\",\"island\",\"i love leetcode\"]
ac.input(' ') -> [\"i love you\",\"i love leetcode\"]
ac.input('a') -> []
ac.input('#') -> []
```""",
        "constraints": "",
        "hint": "Trie keyed by character; each node holds a Counter of sentences passing through it (or you re-aggregate at query time).",
        "starter": """
class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]) -> None:
        raise NotImplementedError

    def input(self, c: str) -> list[str]:
        raise NotImplementedError
""",
        "reference": """
import heapq
from collections import Counter, defaultdict


class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]) -> None:
        self._counts: Counter = Counter()
        for s, t in zip(sentences, times):
            self._counts[s] += t
        self._buf: list[str] = []

    def input(self, c: str) -> list[str]:
        if c == "#":
            sentence = "".join(self._buf)
            self._counts[sentence] += 1
            self._buf.clear()
            return []
        self._buf.append(c)
        prefix = "".join(self._buf)
        candidates = [(-cnt, s) for s, cnt in self._counts.items() if s.startswith(prefix)]
        heapq.heapify(candidates)
        out: list[str] = []
        for _ in range(3):
            if not candidates:
                break
            _, s = heapq.heappop(candidates)
            out.append(s)
        return out
""",
        "tests": """
from solution import AutocompleteSystem


def test_basic_sequence():
    ac = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
    assert ac.input("i") == ["i love you", "island", "i love leetcode"]
    assert ac.input(" ") == ["i love you", "i love leetcode"]
    assert ac.input("a") == []
    assert ac.input("#") == []
""",
    },
    {
        "slug": "18-palindrome-pairs",
        "title": "Palindrome pairs",
        "difficulty": "hard",
        "tags": ["trie", "hash-map", "palindrome"],
        "statement": "Given a list of unique words, return all pairs of distinct indices `(i, j)` such that `words[i] + words[j]` is a palindrome.",
        "signature": "def palindrome_pairs(words: list[str]) -> list[list[int]]: ...",
        "examples_md": """## Examples

| words | result |
|---|---|
| `[\"abcd\",\"dcba\",\"lls\",\"s\",\"sssll\"]` | `[[0, 1], [1, 0], [3, 2], [2, 4]]` |""",
        "constraints": "",
        "hint": "For each word w, split into prefix+suffix at every k. If prefix is palindrome and reverse(suffix) is in the dictionary, that pair works. Map of word -> index for Θ(1) lookup.",
        "starter": """
def palindrome_pairs(words: list[str]) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def palindrome_pairs(words: list[str]) -> list[list[int]]:
    index = {w: i for i, w in enumerate(words)}
    out: list[list[int]] = []

    def _is_pal(s: str) -> bool:
        return s == s[::-1]

    for i, w in enumerate(words):
        for k in range(len(w) + 1):
            pref, suf = w[:k], w[k:]
            if _is_pal(pref):
                rev_suf = suf[::-1]
                if rev_suf != w and rev_suf in index:
                    out.append([index[rev_suf], i])
            if k != len(w) and _is_pal(suf):
                rev_pref = pref[::-1]
                if rev_pref != w and rev_pref in index:
                    out.append([i, index[rev_pref]])
    return out
""",
        "tests": """
from solution import palindrome_pairs


def _norm(pairs):
    return sorted(tuple(p) for p in pairs)


def test_basic():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    assert _norm(palindrome_pairs(words)) == _norm([[0, 1], [1, 0], [3, 2], [2, 4]])


def test_with_empty():
    words = ["a", ""]
    assert _norm(palindrome_pairs(words)) == _norm([[0, 1], [1, 0]])
""",
    },
]
