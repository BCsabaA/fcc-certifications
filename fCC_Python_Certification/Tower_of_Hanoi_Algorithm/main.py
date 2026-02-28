

def hanoi_solver(n: int) -> str:
    def set_hanoi_list(n: int) -> list:
        hanoi_list = []
        numbers = list(range(n,0,-1))
        hanoi_list.append(numbers)
        hanoi_list.append([])
        hanoi_list.append([])
        return hanoi_list

    def start_move(hanoi_list: list) -> list:
        if n % 2 == 0:
            hanoi_list[1].append(hanoi_list[0].pop())
        else:
            hanoi_list[2].append(hanoi_list[0].pop())
        return hanoi_list

    def move_to_str(move: list) -> str:
        return " ".join(str(s) for s in move)+'\n'

    def move(from_list: list, to_list: list, last_item) -> int:
        if len(from_list) == 0:
            return -1
        item_to_move = from_list[-1]
        if item_to_move == last_item:
            return -1
        if len(from_list) > 1 and len(to_list) > 0:
            if from_list[-2] == to_list[-1] - 1:
                return -1
        if to_list == [] or item_to_move < to_list[-1]:
            from_list.pop(-1)
            to_list.append(item_to_move)
            return item_to_move
        return -1

    def next_move(hanoi_list: list, last_item) -> int:
        print(f'{last_item=}')
        # nem mozoghat az utolsó mozgatott elem
        first = hanoi_list[0]
        second = hanoi_list[1]
        third = hanoi_list[2]
        print(f'{first=}')
        print(f'{second=}')
        print(f'{third=}')
        # az elsőt a harmadikra, hanemlehetakkor
        item = move(first, third, last_item)
        # az elsőt a másodikra, hanemlehetakkor
        if item == -1:
             item = move(first, second, last_item)
        # a másodikat a harmadikra, hanemlehetakkor
        if item == -1:
             item = move(second, third, last_item)
        # a harmadikat a másokdikra, hanemlehetakkor
        if item == -1:
             item = move(third, second, last_item)
        # a másodikat az elsőre, hanemlehetakkor
        if item == -1:
             item = move(second, first, last_item)
        return item
            
    
    step = 1
    hanoi_list = set_hanoi_list(n)
    start_list = hanoi_list[0].copy()
    hanoi_solve_moves = move_to_str(hanoi_list)
    start_move(hanoi_list)
    hanoi_solve_moves += move_to_str(hanoi_list)

    escape = ''
    print(f'{start_list=}\n')
    print(f'{step=}')
    print(hanoi_solve_moves)
    step += 1
    last_item_moved = 0

    while start_list != hanoi_list[-1]:
        last_item_moved = next_move(hanoi_list, last_item_moved)
        hanoi_solve_moves += move_to_str(hanoi_list)
        print(f'{step=}')
        print(hanoi_solve_moves)
        step += 1
        print(f'{escape=}')
        print(f'{last_item_moved=}')
        escape = input('q for quit, any other to continue:  ')
        if escape == 'q':
            break







hanoi_solver(4)
# hanoi_solver(4)
# hanoi_solver(5)
# hanoi_solver(6)
# print()
# print('[3, 2, 1] [] []\n[3, 2] [] [1]\n[3] [2] [1]\n[3] [2, 1] []\n[] [2, 1] [3]\n[1] [2] [3]\n[1] [] [3, 2]\n[] [] [3, 2, 1]')
print()
print('[4, 3, 2, 1] [] []\n[4, 3, 2] [1] []\n[4, 3] [1] [2]\n[4, 3] [] [2, 1]\n[4] [3] [2, 1]\n[4, 1] [3] [2]\n[4, 1] [3, 2] []\n[4] [3, 2, 1] []\n[] [3, 2, 1] [4]\n[] [3, 2] [4, 1]\n[2] [3] [4, 1]\n[2, 1] [3] [4]\n[2, 1] [] [4, 3]\n[2] [1] [4, 3]\n[] [1] [4, 3, 2]\n[] [] [4, 3, 2, 1]')
# print()
# print('[5, 4, 3, 2, 1] [] []\n[5, 4, 3, 2] [] [1]\n[5, 4, 3] [2] [1]\n[5, 4, 3] [2, 1] []\n[5, 4] [2, 1] [3]\n[5, 4, 1] [2] [3]\n[5, 4, 1] [] [3, 2]\n[5, 4] [] [3, 2, 1]\n[5] [4] [3, 2, 1]\n[5] [4, 1] [3, 2]\n[5, 2] [4, 1] [3]\n[5, 2, 1] [4] [3]\n[5, 2, 1] [4, 3] []\n[5, 2] [4, 3] [1]\n[5] [4, 3, 2] [1]\n[5] [4, 3, 2, 1] []\n[] [4, 3, 2, 1] [5]\n[1] [4, 3, 2] [5]\n[1] [4, 3] [5, 2]\n[] [4, 3] [5, 2, 1]\n[3] [4] [5, 2, 1]\n[3] [4, 1] [5, 2]\n[3, 2] [4, 1] [5]\n[3, 2, 1] [4] [5]\n[3, 2, 1] [] [5, 4]\n[3, 2] [] [5, 4, 1]\n[3] [2] [5, 4, 1]\n[3] [2, 1] [5, 4]\n[] [2, 1] [5, 4, 3]\n[1] [2] [5, 4, 3]\n[1] [] [5, 4, 3, 2]\n[] [] [5, 4, 3, 2, 1]')
