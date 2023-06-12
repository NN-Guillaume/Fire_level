""" Labyrinthe """

# Créer un programme qui trouve le plus court chemin entre l'entrée et la sortie d'un labyrinthe en évitant les obstacles.

# Le labyrinthe est transmis en argument du programme. 
# La première ligne du labyrinthe contient les informations pour lire la carte : 
#                                                                                   - LIGNESxCOLS
#                                                                                   - caractère plein
#                                                                                   - caractère vide
#                                                                                   - caractère chemin
#                                                                                   - entrée et sortie du labyrinthe.

# Le but du programme est de remplacer les caractères “vide” par des caractères “chemin” pour représenter 
# le plus court chemin pour traverser le labyrinthe. 
# Un déplacement ne peut se faire que vers le haut, le bas, la droite ou la gauche.


"""import sys
import queue

# Class to represent a point in the maze
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# Function to check if a point is within the maze boundaries
def is_valid(row, col, num_rows, num_cols):
    return 0 <= row < num_rows and 0 <= col < num_cols

# Function to check if a point is a valid move in the maze
def is_valid_move(maze, visited, row, col):
    num_rows = len(maze)
    num_cols = len(maze[0])
    return (
        is_valid(row, col, num_rows, num_cols)
        and maze[row][col] != 'solid'
        and not visited[row][col]
    )

# Function to find the shortest path in the maze
def find_shortest_path(maze):
    num_rows = len(maze)
    num_cols = len(maze[0])

    # Extracting information from the maze
    solid_char = maze[0][1]
    empty_char = maze[0][2]
    path_char = maze[0][3]
    entry_point = Point(int(maze[0][4]), int(maze[0][5]))
    exit_point = Point(int(maze[0][6]), int(maze[0][7]))

    # Initializing visited array
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    # Initializing the queue for BFS
    q = queue.Queue()
    q.put(entry_point)

    # BFS traversal
    while not q.empty():
        curr_point = q.get()

        # Check if the current point is the exit point
        if curr_point.row == exit_point.row and curr_point.col == exit_point.col:
            return True

        # Check if the current point is a valid move
        if is_valid_move(maze, visited, curr_point.row, curr_point.col):
            visited[curr_point.row][curr_point.col] = True

            # Update the maze with the path character
            maze[curr_point.row][curr_point.col] = path_char

            # Add the valid neighboring points to the queue
            q.put(Point(curr_point.row - 1, curr_point.col))  # up
            q.put(Point(curr_point.row + 1, curr_point.col))  # down
            q.put(Point(curr_point.row, curr_point.col - 1))  # left
            q.put(Point(curr_point.row, curr_point.col + 1))  # right

    # No path found
    return False

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python feu05.py <maze_file>")
        return

    maze_file = sys.argv[1]

    # Read the maze file and extract the maze
    with open(maze_file, 'r') as file:
        maze = [list(line.strip()) for line in file]

    # Find the shortest path in the maze
    if find_shortest_path(maze):
        print("SORTIE ATTEINTE EN", maze[0][8], "COUPS !")
        print_maze(maze)
    else:
        print("No path found in the maze.")

# Run the main function
if __name__ == '__main__':
    main()"""
####################################################################################################################################
"""import sys
import queue

# Classe pour représenter un point dans le labyrinthe
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# Fonction pour vérifier si un point est dans les limites du labyrinthe
def est_valide(row, col, num_rows, num_cols):
    return 0 <= row < num_rows and 0 <= col < num_cols

# Fonction pour vérifier si un point est un mouvement valide dans le labyrinthe
def est_mouvement_valide(labyrinthe, visite, row, col):
    num_rows = len(labyrinthe)
    num_cols = len(labyrinthe[0])
    return (
        est_valide(row, col, num_rows, num_cols)
        and labyrinthe[row][col] != 'solid'
        and not visite[row][col]
    )

# Fonction pour trouver le plus court chemin dans le labyrinthe
def trouver_plus_court_chemin(labyrinthe):
    num_rows = len(labyrinthe)
    num_cols = len(labyrinthe[0])

    # Extraire les informations du labyrinthe
    caractere_plein = labyrinthe[0][1]
    caractere_vide = labyrinthe[0][2]
    caractere_chemin = labyrinthe[0][3]
    point_entree = Point(int(labyrinthe[0][4]), int(labyrinthe[0][5]))
    point_sortie = Point(int(labyrinthe[0][6]), int(labyrinthe[0][7]))

    # Initialiser le tableau de visite
    visite = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    # Initialiser la file pour le parcours en largeur (BFS)
    file = queue.Queue()
    file.put(point_entree)

    # Parcours en largeur (BFS)
    while not file.empty():
        point_courant = file.get()

        # Vérifier si le point courant est la sortie
        if point_courant.row == point_sortie.row and point_courant.col == point_sortie.col:
            return True

        # Vérifier si le point courant est un mouvement valide
        if est_mouvement_valide(labyrinthe, visite, point_courant.row, point_courant.col):
            visite[point_courant.row][point_courant.col] = True

            # Mettre à jour le labyrinthe avec le caractère chemin
            labyrinthe[point_courant.row][point_courant.col] = caractere_chemin

            # Ajouter les points voisins valides à la file
            file.put(Point(point_courant.row - 1, point_courant.col))  # haut
            file.put(Point(point_courant.row + 1, point_courant.col))  # bas
            file.put(Point(point_courant.row, point_courant.col - 1))  # gauche
            file.put(Point(point_courant.row, point_courant.col + 1))  # droite

    # Aucun chemin trouvé
    return False

# Fonction pour afficher le labyrinthe
def afficher_labyrinthe(labyrinthe):
    for row in labyrinthe:
        print(''.join(row))

# Fonction principale
def main():
    if len(sys.argv) != 2:
        print("Usage: python feu05.py <maze_file>")
        return

    fichier_labyrinthe = sys.argv[1]

    # Lire le fichier du labyrinthe et extraire le labyrinthe
    with open(fichier_labyrinthe, 'r') as fichier:
        labyrinthe = [list(line.strip()) for line in fichier]

    # Trouver le plus court chemin dans le labyrinthe
    if trouver_plus_court_chemin(labyrinthe):
        print("SORTIE ATTEINTE EN", labyrinthe[0][8], "COUPS !")
        afficher_labyrinthe(labyrinthe)
    else:
        print("Aucun chemin trouvé dans le labyrinthe.")

# Exécuter la fonction principale
if __name__ == '__main__':
    main()"""
####################################################################################################################################

import sys
import queue

# Classe pour représenter un point dans le labyrinthe
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# Fonction pour vérifier si un point est dans les limites du labyrinthe
def est_valide(row, col, num_rows, num_cols):
    return 0 <= row < num_rows and 0 <= col < num_cols

# Fonction pour vérifier si un point est un mouvement valide dans le labyrinthe
def est_mouvement_valide(labyrinthe, visite, row, col):
    num_rows = len(labyrinthe)
    num_cols = len(labyrinthe[0])
    return (
        est_valide(row, col, num_rows, num_cols)
        and labyrinthe[row][col] != '*'
        and not visite[row][col]
    )

# Fonction pour trouver le plus court chemin dans le labyrinthe
def trouver_plus_court_chemin(labyrinthe):
    num_rows = len(labyrinthe)
    num_cols = len(labyrinthe[0])

    # Extraire les informations du labyrinthe
    caractere_plein = labyrinthe[0][1]
    caractere_vide = labyrinthe[0][2]
    caractere_chemin = labyrinthe[0][3]
    point_entree = Point(int(labyrinthe[0][4]), int(labyrinthe[0][5]))
    point_sortie = Point(int(labyrinthe[0][6]), int(labyrinthe[0][7]))

    # Initialiser le tableau de visite
    visite = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    # Initialiser la file pour le parcours en largeur (BFS)
    file = queue.Queue()
    file.put(point_entree)

    # Parcours en largeur (BFS)
    while not file.empty():
        point_courant = file.get()

        # Vérifier si le point courant est la sortie
        if point_courant.row == point_sortie.row and point_courant.col == point_sortie.col:
            return True

        # Vérifier si le point courant est un mouvement valide
        if est_mouvement_valide(labyrinthe, visite, point_courant.row, point_courant.col):
            visite[point_courant.row][point_courant.col] = True

            # Mettre à jour le labyrinthe avec le caractère chemin
            labyrinthe[point_courant.row][point_courant.col] = caractere_chemin

            # Ajouter les points voisins valides à la file
            file.put(Point(point_courant.row - 1, point_courant.col))  # haut
            file.put(Point(point_courant.row + 1, point_courant.col))  # bas
            file.put(Point(point_courant.row, point_courant.col - 1))  # gauche
            file.put(Point(point_courant.row, point_courant.col + 1))  # droite

    # Aucun chemin trouvé
    return False

# Fonction pour afficher le labyrinthe
def afficher_labyrinthe(labyrinthe):
    for row in labyrinthe:
        print(''.join(row))

# Fonction principale
def main():
    if len(sys.argv) != 2:
        print("Usage: python maze_solver.py <maze_file>")
        return

    fichier_labyrinthe = sys.argv[1]

    # Lire le fichier du labyrinthe et extraire le labyrinthe
    with open(fichier_labyrinthe, 'r') as fichier:
        labyrinthe = [list(line.strip()) for line in fichier]

    # Afficher le labyrinthe de base
    print("Base maze:")
    afficher_labyrinthe(labyrinthe)
    print()

    # Trouver le plus court chemin dans le labyrinthe
    if trouver_plus_court_chemin(labyrinthe):
        # Afficher le labyrinthe résolu
        print("Solved maze:")
        afficher_labyrinthe(labyrinthe)
    else:
        print("Aucun chemin trouvé dans le labyrinthe.")

# Exécuter la fonction principale
if __name__ == '__main__':
    main()
