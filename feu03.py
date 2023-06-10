""" Sudoku """

# Créer un programme qui trouve et affiche la solution d'un sudoku

""" Here we go again with a dumb useless shit . . . """

#   $> cat sudoku.txt                   $> python feu03.py

#   1 9 5 7 8 4 2 . .                   1 9 5 7 8 4 2 6 3
#   3 . 6 5 2 9 1 4 7                   3 8 6 5 2 9 1 4 7             
#   4 7 2 1 . 3 9 8 5                   4 7 2 1 6 3 9 8 5
#   6 3 7 8 5 2 4 1 9                   6 3 7 8 5 2 4 1 9
#   8 5 9 6 . 1 7 3 2                   8 5 9 6 4 1 7 3 2
#   2 1 4 3 9 7 6 5 8                   2 1 4 3 9 7 6 5 8
#   9 2 . 4 1 8 5 7 6                   9 2 3 4 1 8 5 7 6
#   5 . 8 9 7 6 3 2 1                   5 4 8 9 7 6 3 2 1
#   7 6 1 2 3 5 8 . 4                   7 6 1 2 3 5 8 9 4

# first, test on a simple grid
#   1 2 3
#   2 3 1
#   3 1 2

def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for num in range(1, 10):
                    if is_valid(board, row, col, str(num)):
                        board[row][col] = str(num)

                        if solve_sudoku(board):
                            return True

                        board[row][col] = '.'

                return False

    return True

def read_sudoku_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    sudoku = [[None] * 9 for _ in range(9)]
    for i in range(9):
        line = lines[i].strip().split()
        for j in range(9):
            sudoku[i][j] = line[j]

    return sudoku

def print_sudoku(board):
    for row in board:
        print(' '.join(row))

def main():
    file_name = 'sudoku.txt'  # Change this to the name of your file if needed

    # Read Sudoku puzzle from file
    sudoku = read_sudoku_from_file(file_name)

    print("Sudoku puzzle:")
    print_sudoku(sudoku)
    print()

    # Solve Sudoku puzzle
    if solve_sudoku(sudoku):
        print("Solution:")
        print_sudoku(sudoku)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == '__main__':
    main()
