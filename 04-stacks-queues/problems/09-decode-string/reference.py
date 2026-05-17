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
