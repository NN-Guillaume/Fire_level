import sys
import random

"""
Here is where you start !

1°) create a plate with the code below.

2°) copy and paste the plate in the plate.txt file (create it if it doesn't exist)

3°) run the code in the feu04.py to solve the plate !
"""

# Generate a plate to use the code of the file feu04.py
def plate_generator(x, y, density):

    if len(sys.argv) != 4:
        print("params needed: x y density")
        exit()

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    density = int(sys.argv[3])

    print(f"{y}.xo")
    for i in range(y+1):
        for j in range(x+1):
            print('x' if random.randint(0, y*2) < density else '.', end='')
        print()

plate_generator(sys.argv[1], sys.argv[2], sys.argv[3])

# exemple of use --->   $> python feu04_gen.py 10 10 10

# exemple of result (be sure to respect each space on the first row !)

#   10 . x o
#   .xx.xxxx...
#   xxxx.x.x.x.
#   .x..x......
#   .......x.x.
#   ......x..x.
#   ......xx..x
#   .x.xx......
#   xx..xxxx...
#   xx.xx..x..x
#   x.x...x...x
#   x.xx..x.xx.