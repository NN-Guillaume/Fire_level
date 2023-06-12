""" Trouver le plus grand carré """

# Créer un programme qui remplace les caractères vides par des caractères plein pour représenter le plus grand carré possible sur un plateau.
# Le plateau sera transmis dans un fichier.
# La première ligne du fichier contient les informations pour lire la carte:
#                                                                           - nombre de lignes du plateau
#                                                                           - caractères pour "vide"
#                                                                           - caractères pour "obstacle"
#                                                                           - caractères pour "plein"

"""
Please, follow the instructions below:

1°) create a plate with the code in the file feu04_gen.py.

2°) copy and paste the plate in the plate.txt file (create it if it doesn't exist)

3°) run the code in the feu04.py to solve the plate !
"""

def read_plate(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return None
    except:
        print("An error occurred while reading the file.")
        return None
    
    # Validate the plate/board
    if not validate_plate(lines):
        return None
    
    # Extract plate/board information
    row_count, empty_char, obstacle_char, filled_char = lines[0].split()
    row_count = int(row_count)
    
    # Remove the first line from the plate
    plate = [line.strip() for line in lines[1:]]
    
    return row_count, empty_char, obstacle_char, filled_char, plate


def validate_plate(lines):
    if len(lines) < 2:
        print("Invalid plate/board format. Missing lines.")
        return False
    
    # Check if all lines have the same length
    line_length = len(lines[1].strip())
    for line in lines[1:]:
        if len(line.strip()) != line_length:
            print("Invalid plate/board format. Lines have different lengths.")
            return False
    
    # Check if all characters are from the first line
    first_line_chars = set(lines[1].strip())
    for line in lines[2:]:
        chars = set(line.strip())
        if chars != first_line_chars:
            print("Invalid plate/board format. Characters are not consistent.")
            return False
    
    return True


def find_largest_square(plate):
    row_count = len(plate)
    col_count = len(plate[0])
    max_square_size = 0
    max_square_row = 0
    max_square_col = 0
    
    # Create a 2D matrix to store the size of the largest square ending at each cell
    sizes = [[0] * col_count for _ in range(row_count)]
    
    # Compute the sizes of the largest square for each cell
    for i in range(1, row_count):
        for j in range(1, col_count):
            if plate[i][j] == empty_char:
                sizes[i][j] = min(sizes[i-1][j], sizes[i][j-1], sizes[i-1][j-1]) + 1
                if sizes[i][j] > max_square_size:
                    max_square_size = sizes[i][j]
                    max_square_row = i
                    max_square_col = j
    
    # Replace the empty characters with 'o' to represent the largest square
    for i in range(max_square_row, max_square_row - max_square_size, -1):
        for j in range(max_square_col, max_square_col - max_square_size, -1):
            plate[i] = plate[i][:j] + filled_char + plate[i][j+1:]
    
    return plate


def print_plate(plate):
    for row in plate:
        print(row)


# Read the plate/board from the file
file_name = "plate.txt"
plate_info = read_plate(file_name)
if plate_info is not None:
    row_count, empty_char, obstacle_char, filled_char, plate = plate_info
    
    # Find the largest square and update the plate
    modified_plate = find_largest_square(plate)
    
    # Print the modified plate/board
    print_plate(modified_plate)
