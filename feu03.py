""" Sudoku """

# Créer un programme qui trouve et affiche la solution d'un sudoku

""" Here we go again with a dumb useless shit . . . """

#   $> sudoku.txt                       $> python feu03.py

#   1 9 5 7 8 4 2 . .                   1 9 5 7 8 4 2 6 3
#   3 . 6 5 2 9 1 4 7                   3 8 6 5 2 9 1 4 7             
#   4 7 2 1 . 3 9 8 5                   4 7 2 1 6 3 9 8 5
#   6 3 7 8 5 2 4 1 9                   6 3 7 8 5 2 4 1 9
#   8 5 9 6 . 1 7 3 2                   8 5 9 6 4 1 7 3 2
#   2 1 4 3 9 7 6 5 8                   2 1 4 3 9 7 6 5 8
#   9 2 . 4 1 8 5 7 6                   9 2 3 4 1 8 5 7 6
#   5 . 8 9 7 6 3 2 1                   5 4 8 9 7 6 3 2 1
#   7 6 1 2 3 5 8 . 4                   7 6 1 2 3 5 8 9 4

# check if a value is already present in the same row, same column and same 3x3 box. 
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

    # If the value is a potenial/good one, then it returns True
    return True

# Use recursive funcion (the one above) to solve the sudoku.
def solve_sudoku(board):
    # Iterate through each cell in the board
    for row in range(9):
        for col in range(9):
            # Check if the cell is empty
            if board[row][col] == '.':
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    # Check if the number is a valid choice for the cell
                    if is_valid(board, row, col, str(num)):
                        # If valid, assign the number to the cell
                        board[row][col] = str(num)

                        # Recursively solve the remaining part of the puzzle
                        if solve_sudoku(board):
                            return True

                        # If the recursive call returns False, backtrack by undoing the assignment
                        board[row][col] = '.'

                # If no valid number leads to a solution, return False
                return False

    # If all cells are filled, the puzzle is solved
    return True


# read the txt file, create a 2D list where the puzzle is stored and return the sudoku list (see function below)
def read_sudoku_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # creates a 2D list named sudoku with 9 rows and 9 columns, initially filled with None values.
    sudoku = [[None] * 9 for _ in range(9)]
    # iterates through each line (representing each row in the Sudoku puzzle)
    for i in range(9):
        # For each line, it removes any leading or trailing whitespace using the strip method and splits the line into 
        # individual numbers using the split method. 
        # The result is stored in the line variable.
        # For each line, it removes any leading or trailing whitespace using the strip method and splits the 
        # line into individual numbers using the split method. The result is stored in the line variable.
        # It iterates through the numbers in the line list and assigns them to the corresponding positions in the sudoku list.
        line = lines[i].strip().split()
        for j in range(9):
            sudoku[i][j] = line[j]

    # Finally, it returns the sudoku list representing the Sudoku puzzle.
    return sudoku

# return the sudoku list
def print_sudoku(board):
    for row in board:
        print(' '.join(row))

# Here we manage and use all the functions defined above
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
