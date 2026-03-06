def hanoi(n: int) -> str:
    hanoi_str = ''

    def step_to_hanoi_str() -> None:
        nonlocal hanoi_str
        hanoi_str += '\n' + str(first) + ' ' + str(second) + ' ' + str(third)
        

    def hanoi_solve(n, source: list, target: list, auxiliary: list) -> None:
        if n == 1:
            source.pop(-1)
            target.append(1)
            step_to_hanoi_str()
            return
        hanoi_solve(n-1, source, auxiliary, target)
        source.pop(-1)
        target.append(n)
        step_to_hanoi_str()
        hanoi_solve(n-1, auxiliary, target, source)
    
    first = list(range(n, 0, -1))
    second = []
    third = []

    hanoi_str = str(first) + ' ' + str(second) + ' ' + str(third)

    hanoi_solve(n, first, third, second)

    return hanoi_str

print(hanoi(4))
