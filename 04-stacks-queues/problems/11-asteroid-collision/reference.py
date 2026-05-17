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
