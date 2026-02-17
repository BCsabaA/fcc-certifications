

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

    def next_move(hanoi_list: list, last_item) -> int:
        print(f'{last_item=}')
        # nem mozoghat az utolsó mozgatott elem
        left = hanoi_list[0]
        middle = hanoi_list[1]
        right = hanoi_list[2]
        print(left)
        print(middle)
        print(right)
        # kezdés:
        #     páratlan az elsőt a harmadikra
        #     páros az elsőt a másodikra
        # az elsôt az harmadikra, hanemlehetakkor
        # az elsőt a másodikra, hanemlehetakkor
        # a másodikat a harmadikra, hanemlehetakkor
        # a harmadikat a másokdikra, hanemlehetakkor
        # a másodikat az elsőre, hanemlehetakkor
        # a harmadikat az elsőre
        
            
        
    hanoi_list = set_hanoi_list(n)
    start_list = hanoi_list[0].copy()
    hanoi_solve_moves = move_to_str(hanoi_list)
    start_move(hanoi_list)
    hanoi_solve_moves += move_to_str(hanoi_list)

    escape = ''
    print(f'{start_list=}\n')
    print(hanoi_solve_moves)
    last_item_moved = 0

    while start_list != hanoi_list[-1]:
        last_item_moved = next_move(hanoi_list, last_item_moved)
        hanoi_solve_moves += move_to_str(hanoi_list)
        print(hanoi_solve_moves)
        print(f'{escape=}')
        print(f'{last_item_moved=}')
        escape = input('q for quit, any other to continue:  ')
        if escape == 'q':
            break







hanoi_solver(3)
# hanoi_solver(4)
# hanoi_solver(5)
# hanoi_solver(6)
# print()
# print('[3, 2, 1] [] []\n[3, 2] [] [1]\n[3] [2] [1]\n[3] [2, 1] []\n[] [2, 1] [3]\n[1] [2] [3]\n[1] [] [3, 2]\n[] [] [3, 2, 1]')
# print()
# print('[4, 3, 2, 1] [] []\n[4, 3, 2] [1] []\n[4, 3] [1] [2]\n[4, 3] [] [2, 1]\n[4] [3] [2, 1]\n[4, 1] [3] [2]\n[4, 1] [3, 2] []\n[4] [3, 2, 1] []\n[] [3, 2, 1] [4]\n[] [3, 2] [4, 1]\n[2] [3] [4, 1]\n[2, 1] [3] [4]\n[2, 1] [] [4, 3]\n[2] [1] [4, 3]\n[] [1] [4, 3, 2]\n[] [] [4, 3, 2, 1]')
# print()
# print('[5, 4, 3, 2, 1] [] []\n[5, 4, 3, 2] [] [1]\n[5, 4, 3] [2] [1]\n[5, 4, 3] [2, 1] []\n[5, 4] [2, 1] [3]\n[5, 4, 1] [2] [3]\n[5, 4, 1] [] [3, 2]\n[5, 4] [] [3, 2, 1]\n[5] [4] [3, 2, 1]\n[5] [4, 1] [3, 2]\n[5, 2] [4, 1] [3]\n[5, 2, 1] [4] [3]\n[5, 2, 1] [4, 3] []\n[5, 2] [4, 3] [1]\n[5] [4, 3, 2] [1]\n[5] [4, 3, 2, 1] []\n[] [4, 3, 2, 1] [5]\n[1] [4, 3, 2] [5]\n[1] [4, 3] [5, 2]\n[] [4, 3] [5, 2, 1]\n[3] [4] [5, 2, 1]\n[3] [4, 1] [5, 2]\n[3, 2] [4, 1] [5]\n[3, 2, 1] [4] [5]\n[3, 2, 1] [] [5, 4]\n[3, 2] [] [5, 4, 1]\n[3] [2] [5, 4, 1]\n[3] [2, 1] [5, 4]\n[] [2, 1] [5, 4, 3]\n[1] [2] [5, 4, 3]\n[1] [] [5, 4, 3, 2]\n[] [] [5, 4, 3, 2, 1]')
