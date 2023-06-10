""" Trouver une forme """

# Créer un programme qui affiche la position de lélément le plus en haut à gauche (dans l'ordre) d'une forme au seins d'un plateau.

""" ? ? ? """

""" Here we go again with a dumb useless shit . . . """

#exemple

# 0000      ----
# 1111      --11
# 2331      ---1
#
# yup, this shit is as useless as senseless

def read_board(file_path):
    """
    Reads the board from a text file and returns it as a list of strings.
    Each string represents a row of the board.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def read_shape(file_path):
    """
    Reads the shape from a text file and returns it as a list of strings.
    Each string represents a row of the shape.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_shape(board, shape):
    """
    Finds the position of the top-left occurrence of the shape within the tray.
    Returns the coordinates (row, column) if found, or None if not found.
    """
    rows = len(board)              # Number of rows in the board
    cols = len(board[0])           # Number of columns in the board
    shape_rows = len(shape)        # Number of rows in the shape
    shape_cols = len(shape[0])     # Number of columns in the shape

    # Iterate over possible positions to search for the shape
    for i in range(rows - shape_rows + 1):
        for j in range(cols - shape_cols + 1):
            found = True  # Flag to indicate if the shape is found at this position

            # Check if each element of the shape matches the corresponding element in the board
            for k in range(shape_rows):
                for l in range(shape_cols):
                    if shape[k][l] != board[i + k][j + l]:
                        found = False  # Found a mismatch, shape is not found at this position
                        break
                if not found:
                    break

            if found:
                return i, j  # Shape found, return the top-left coordinates

    return None  # Shape not found

def display_result(board, shape, position):
    """
    Displays the result of the shape search.
    If the shape is found, it prints the position and highlights the shape in the board.
    """
    if position is not None:  # If shape is found
        print("Trouvé !")
        print("Coordonnées:", position[0] + 1, position[1] + 1)  # Convert zero-based indexing to one-based
        print("----")

        for i in range(len(board)):
            row = list(board[i])

            # Highlight the shape by replacing corresponding elements in the board
            if i >= position[0] and i < position[0] + len(shape):
                for j in range(len(shape[0])):
                    row[position[1] + j] = shape[i - position[0]][j]

            print("".join(row))  # Print the modified row of the board
    else:
        print("Non trouvé.")  # Shape not found

if __name__ == "__main__":
    # Prompt the user to enter the file paths for the board and shape.
    board_file = 'board.txt'
    shape_file = 'to_find.txt'

    # Read the board and shape from the specified files.
    board = read_board(board_file)
    shape = read_shape(shape_file)

    # Search for the shape within the board.
    position = find_shape(board, shape)

    # Display the search result.
    display_result(board, shape, position)

    """
    # 1 The program starts with three helper functions: read_board, read_shape, and find_shape.

    # 2 The read_board function reads the board from a text file. It opens the file, reads each line, and strips any leading or trailing whitespace characters. It returns the board as a list of strings, where each string represents a row of the board.

    # 3 The read_shape function reads the shape from a text file. It follows the same approach as read_board and returns the shape as a list of strings, where each string represents a row of the shape.

    # 4 The find_shape function takes the board and the shape as input and searches for the top-left occurrence of the shape within the tray. It uses nested loops to iterate over all possible positions where the shape could be found.

    # 5 The find_shape function compares the shape with the corresponding elements in the board. If any element in the shape does not match the corresponding element in the board, it breaks out of the inner loop and moves to the next position.

    # 6 If a match is found, the function returns the coordinates of the top-left element of the shape within the tray (i, j). The coordinates are zero-based, so the actual position would be (i+1, j+1).

    # 7 If no match is found, the function returns None.

    # 8 The display_result function takes the board, shape, and position as input and displays the result of the shape search. If the position is not None, it prints "Trouvé !" (Found!) along with the coordinates. It then iterates over each row of the board, replacing the elements in the highlighted shape area with the corresponding elements from the shape. Finally, it prints the modified board.

    # 9 In the if __name__ == "__main__": block, the program prompts the user to enter the file paths for the board and shape.

    # 10 It calls the read_board and read_shape functions to read the board and shape from the specified files.

    # 11 It calls the find_shape function to search for the shape within the board.

    # 12 Finally, it calls the display_result function to display the search result.

By following this logic, the program reads the board and shape from files, searches for the shape within the board, and displays the result with the coordinates and the modified board.
    """