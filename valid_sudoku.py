def is_repeated(board, lin, col):
    for i in range(9):
        if i != lin and board[i][col] == board[lin][col]:
            return True

        if i != col and board[lin][i] == board[lin][col]:
            return True

    base_lin = (lin // 3) * 3
    base_col = (col // 3) * 3
    for i in range(base_lin, base_lin + 3):
        for j in range(base_col, base_col + 3):
            if i == lin and j == col:
                continue
            if board[i][j] == board[lin][col]:
                return True

    return False


def is_valid_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != "." and is_repeated(board, i, j):
                return False
    return True


if __name__ == '__main__':
    sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(is_valid_sudoku(sudoku))

    sudoku = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(is_valid_sudoku(sudoku))
