#complexity O(M∗N)
def set_zeroes(matrix) -> None:
    matrix_size = len(matrix)
    if matrix_size == 0:
        return

    zero_position_line_dic = dict()
    zero_position_column_dic = dict()
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            if matrix[line][column] == 0:
                zero_position_line_dic[line] = line
                zero_position_column_dic[column] = column

    for line in range(len(matrix)):
        line_zero = zero_position_line_dic.get(line, -1)
        for column in range(len(matrix[line])):
            if line_zero >= 0:
                matrix[line][column] = 0
            else:
                column_zero = zero_position_column_dic.get(column, -1)
                if column_zero == column:
                    matrix[line][column] = 0


if __name__ == '__main__':
    matrix_param = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix_param)
    print(f"matrix with zeros: {matrix_param}")
    matrix_param = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(matrix_param)
    print(f"matrix with zeros: {matrix_param}")
