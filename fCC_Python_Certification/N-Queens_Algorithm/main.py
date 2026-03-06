def rotate_matrix(matrix):
    pass

def matrix_data_of_coord(matrix: list[list], coord: tuple) -> dict:

    def matrix_diagonal1_of_coord(matrix: list[list], coord: tuple) -> int:
        coord_x = coord[0]
        coord_y = coord[1]
        diagonal1_sum = 0
        diagonal1_sum += matrix[coord_y][coord_x]

        d_coord_x = coord_x - 1
        d_coord_y = coord_y - 1
        while d_coord_x >= 0 and d_coord_y >= 0:
            diagonal1_sum += matrix[d_coord_y][d_coord_x]
            d_coord_x = d_coord_x - 1
            d_coord_y = d_coord_y - 1

        d_coord_x = coord_x + 1
        d_coord_y = coord_y + 1
        while d_coord_x < len(matrix) and d_coord_y < len(matrix):
            diagonal1_sum += matrix[d_coord_y][d_coord_x]
            d_coord_x = d_coord_x + 1
            d_coord_y = d_coord_y + 1
        return diagonal1_sum

    line_sum = 0
    column_sum = 0
    coord_x = coord[0]
    coord_y = coord[1]

    # line sum
    line_sum = sum(matrix[coord_y])

    # column sum 
    for y in range(len(matrix)):
        column_sum += matrix[y][coord_x]

    #diagonal 1 sum: top-left to bottom-right
    diagonal1_sum = matrix_diagonal1_of_coord(matrix, coord)

    #diagonal 2 sum: top-right to bottom-left
    diagonal1_sum = matrix_diagonal1_of_coord(matrix, coord)
    n = len(matrix)
    rotate_matrix = []
    for i in range(n):
        line = [0] * n
        rotate_matrix.append(line)

    for i in range(n):
        for j in range(n):
            rotate_matrix[n-j-1][i] = matrix[i][j]

    rotate_coord = (coord_y, n-coord_x-1)
    diagonal2_sum = matrix_diagonal1_of_coord(
        rotate_matrix,
        rotate_coord)

    return {
        'line_sum': line_sum ,
        'column_sum': column_sum,
        'diagona1_sum': diagonal1_sum,
        'diagona2_sum': diagonal2_sum,
        'total': line_sum +
        column_sum + diagonal1_sum + diagonal2_sum
    }

def print_matrix(matrix):
    for line in matrix:
        print(line)


def dfs_n_queens(n):
    if n < 1:
        return []
    
    adj_matrix = []
    for i in range(n):
        adj_matrix.append([0] * n)
    solutions = []
    solution = []

    start_coord = (0,0)
    stack = [start_coord]
    visited = [start_coord]

    print_matrix(adj_matrix)

    while stack:
        print(f'{start_coord=}')
        print(f'{stack=}')
        actual_coord_x, actual_coord_y = stack.pop()
        print(f'{visited=}')
        print(f'{actual_coord_x=}')
        print(f'{actual_coord_y=}')

        if matrix_data_of_coord(adj_matrix, (actual_coord_x, actual_coord_y))['total'] == 0:
            adj_matrix[actual_coord_y][actual_coord_x] = 1
            print_matrix(adj_matrix)
            solution.append(actual_coord_y)

        if actual_coord_y + 1 < len(adj_matrix):
            new_coord_y = actual_coord_y + 1
            new_coord_x = actual_coord_x
            new_coord = (new_coord_x, new_coord_y)
            print(f'{new_coord=}')
            stack.append(new_coord)
            visited.append(new_coord)
        else:
            if actual_coord_x + 1 < len(adj_matrix):
                new_coord_x = actual_coord_x + 1
                new_coord_y = 0
                new_coord = (new_coord_x, new_coord_y)
                print(f'{new_coord=}')
                stack.append(new_coord)
                visited.append(new_coord)
            else:
                print(f'{solution=}')
                if len(solution) == n:
                    solutions.append(solution)
                print(f'{solutions=}')
                if start_coord[1] + 1 < len(adj_matrix):
                    start_coord = (start_coord[0], start_coord[1] + 1)
                    print(f'new {start_coord=}')
                    stack = [start_coord]
                    visited = [start_coord]
                else:
                    return solutions


        








































    #     print(f'{stack=}')
    #     print(f'{visited=}')
    #     act_coord = stack.pop()
    #     print(f'{act_coord=}')
    #     print_matrix(adj_matrix)
    #     act_coord_x = act_coord[0]
    #     act_coord_y = act_coord[1]
    #     if matrix_data_of_coord(adj_matrix, act_coord)['total'] == 0:
    #         adj_matrix[act_coord_y][act_coord_x] = 1
    #         solution.append(act_coord_y)
    #     new_coord_x = 0
    #     new_coord_y = 0
    #     print(f'{len(adj_matrix)=}')
    #     print(f'{act_coord_x=}')
    #     print(f'{act_coord_y=}')

    #     if act_coord_x + 1 < len(adj_matrix):
    #         new_coord_x = act_coord_x + 1
    #         new_coord_y = act_coord_y
    #         print(f'{new_coord_x=}')
    #     else:
    #         new_coord_x = 0
    #         if act_coord_y + 1 < len(adj_matrix):
    #             new_coord_y = act_coord_y + 1
    #             print(f'{new_coord_y=}')
    #         else:
    #             stack = []
    #             visited = []
    #             if len(solution) == n:
    #                 solutions.append(solution)
    #             solution = []
    #             start_coord_x = start_coord[0]
    #             start_coord_y = start_coord[1]
    #             if start_coord_x + 1 < len(adj_matrix):
    #                 new_coord_x = start_coord_x + 1
    #             else:
    #                 start_coord = (start_coord_x, start_coord_y)
    #                 break
    #             new_coord_y = 0
    #     new_coord = (new_coord_x, new_coord_y)
    #     print(f'{new_coord=}')
    #     if new_coord not in visited:
    #         stack.append(new_coord)
    #         visited.append(new_coord)
            
    # # if len(solution) == n:
    # #     solutions.append(solution)



    # # for y in range(n):
    # #     for x in range(n):
    # #         print_matrix(adj_matrix)
    # #         print(solution)
    # #         if matrix_data_of_coord(
    # #                 adj_matrix, (x, y))['total'] == 0:
    # #             solution.append(y)
    # #             adj_matrix[x][y] = 1
    # #             break
    # # return solution

n = 4

print(dfs_n_queens(n))

#print(adj_matrix)

# matrix = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# print_matrix(matrix)

# for x in range(len(adj_matrix)):
#     for y in range(len(adj_matrix)):
#         coord = (x, y)
#         print(coord, matrix_data_of_coord(matrix, coord)['total'])

# print(matrix_data_of_coord, coord)
