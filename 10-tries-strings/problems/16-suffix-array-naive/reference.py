def suffix_array(s: str) -> list[int]:
    return sorted(range(len(s)), key=lambda i: s[i:])
