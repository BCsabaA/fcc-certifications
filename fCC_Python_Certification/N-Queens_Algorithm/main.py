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
    diagonal2_sum = matrix_diagonal1_of_coord(rotate_matrix, rotate_coord)

    return {
        'line_sum': line_sum ,
        'column_sum': column_sum,
        'diagona1_sum': diagonal1_sum,
        'diagona2_sum': diagonal2_sum,
        'total': line_sum + column_sum + diagonal1_sum + diagonal2_sum
    }

n = 2

adj_matrix = [[0] * n] * n
print(adj_matrix)



for x in range(len(adj_matrix)):
    for y in range(len(adj_matrix)):
        coord = (x, y)
        print(coord)
        print(matrix_data_of_coord(adj_matrix, coord))

# print(matrix_data_of_coord, coord)