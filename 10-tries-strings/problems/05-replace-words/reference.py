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
