def hanoi(n: int) -> str:
    hanoi_str = ''
    step = 1

    def hanoi_solve(n, source: list, target: list, auxiliary: list, mode: 1) -> None:
        nonlocal step
        nonlocal hanoi_str
        # print(f'{source} {auxiliary} {target}')
        if n == 1:
            print(f'{step=}')
            print(f'{mode=}')
            print(hanoi_str)
            source.pop(-1)
            target.append(1)
            step += 1
            if mode == 1:
                hanoi_str = str(source) + ' ' + str(auxiliary) + ' ' + str(target)
            if mode == 2:
                hanoi_str = str(source) + ' ' + str(target) + ' ' + str(auxiliary)
            if mode == 3:
                hanoi_str = str(auxiliary) + ' ' + str(source) + ' ' + str(target)
            return
        hanoi_solve(n-1, source, auxiliary, target, 2)
        print(f'{step=}')
        print(f'{mode=}')
        print(hanoi_str)
        source.pop(-1)
        target.append(n)
        step += 1
        if mode == 1:
            hanoi_str = str(source) + ' ' + str(auxiliary) + ' ' + str(target)
        if mode == 2:
            hanoi_str = str(source) + ' ' + str(target) + ' ' + str(auxiliary)
        if mode == 3:
            hanoi_str = str(auxiliary) + ' ' + str(source) + ' ' + str(target)
        hanoi_solve(n-1, auxiliary, target, source, 3)
    
    first = list(range(n, 0, -1))
    second = []
    third = []

    hanoi_str = str(first) + ' ' + str(second) + ' ' + str(third)

    hanoi_solve(n, first, third, second, 1)

    print(hanoi_str)

hanoi(3)
