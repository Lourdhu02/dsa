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
