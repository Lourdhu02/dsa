def repeated_substring_pattern(s: str) -> bool:
    return s in (s + s)[1:-1]
