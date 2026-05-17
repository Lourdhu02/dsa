def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    stack: list[float] = []
    for p, s in cars:
        t = (target - p) / s
        if not stack or t > stack[-1]:
            stack.append(t)
    return len(stack)
