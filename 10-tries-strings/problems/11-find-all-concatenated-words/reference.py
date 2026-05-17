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
