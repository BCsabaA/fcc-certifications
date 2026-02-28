def hanoi(n: int) -> str:

    def hanoi_solve(n, source: list, target: list, auxiliary: list) -> None:
        print(f'{source   =}')
        print(f'{auxiliary=}')
        print(f'{target   =}')
        if n == 1:
            source.pop(-1)
            target.append(n)
            return
        hanoi_solve(n-1, source, auxiliary, source)
        hanoi_solve(n-1, auxiliary, target, source)
    
    first = list(range(n, 0, -1))
    second = []
    third = []
    print('start')
    print(f'{first =}')
    print(f'{second=}')
    print(f'{third =}')

    hanoi_solve(n, first, third, second)

    print('finish')
    print(f'{first =}')
    print(f'{second=}')
    print(f'{third =}')

hanoi(2)
