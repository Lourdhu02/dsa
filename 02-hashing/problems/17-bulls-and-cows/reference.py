from collections import Counter


def get_hint(secret: str, guess: str) -> str:
    bulls = sum(s == g for s, g in zip(secret, guess))
    sc: Counter = Counter()
    gc: Counter = Counter()
    for s, g in zip(secret, guess):
        if s != g:
            sc[s] += 1
            gc[g] += 1
    cows = sum((sc & gc).values())
    return f"{bulls}A{cows}B"
