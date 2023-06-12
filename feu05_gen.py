import random

"""def maze_generator(height, width, chars):
    if len(chars) < 5:
        print("characters should have at least 5 characters")
    else:
        height, width = int(height), int(width)
        entry = random.randint(2, width - 4)
        entry2 = random.randint(2, width - 4)
        print(f"{height}x{width}{chars}")
        for y in range(height):
            for x in range(width):
                if y == 0 and x == entry:
                    print(chars[3], end='')
                elif y == height - 1 and x == entry2:
                    print(chars[4], end='')
                elif 1 <= y <= height - 2 and 1 <= x <= width - 2 and random.randint(0, 100) > 20:
                    print(chars[1], end='')
                else:
                    print(chars[0], end='')
            print()

maze_generator(10, 10, "* o12$")"""


def generate_maze(height, width, solid_char, empty_char, path_char, entry_char, exit_char):
    maze = []
    for _ in range(height):
        row = [solid_char] * width
        maze.append(row)

    maze[1][1] = entry_char
    maze[height-2][width-2] = exit_char

    for i in range(2, height-2):
        for j in range(2, width-2):
            if random.randint(0, 100) > 20:
                maze[i][j] = empty_char

    return maze

# Generate a maze
height = 10
width = 10
solid_char = '*'
empty_char = ' '
path_char = 'o'
entry_char = '1'
exit_char = '2'
maze = generate_maze(height, width, solid_char, empty_char, path_char, entry_char, exit_char)

# Save the maze to a file
with open('maze.map', 'w') as file:
    file.write(f'{height}x{width} {solid_char} {empty_char} {path_char} {entry_char} {exit_char}\n')
    for row in maze:
        file.write(''.join(row) + '\n')

