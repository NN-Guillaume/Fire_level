""" Echauffement """

# Créer un programme qui affiche un rectangle dans le terminal.

# L'argument n°1 dessine horizontalement et l'argument n°2 dessine verticalement.

# feu00.py 5 3     arg1         o---o                feu00.py 5 1                    o---o                       feu00.py 1 1            o
#                  arg2         |   |
#                  arg1         o---o


import sys


def draw_geometric(val1, val2):
    draw_up_line(val1)
    draw_each_side_lines(val1, val2)
    #draw_side_line(val1 ,val2)
    draw_down_line(val1)


def draw_down_line(val1):
    if val1 == 0:
        print(" can't draw anything")
    elif val1 == 1:
        print("o")
    elif val1 == 2:
        print("oo")
    elif val1 >= 2:
        #algo
        spe = '-'
        print("o" + (spe * (val1 - 2)) + "o")
        #...
    else:
        print(" unexpected event ")


def draw_each_side_lines(val1, val2):
    lineNumber = val2 - 2
    count = 0
    
    while count != lineNumber:
        draw_side_line(val1, val2)
        count += 1
        
        if count == lineNumber:
            break
        else:
            continue


def draw_side_line(val1, val2):
    if val2 == 0:
        print(" can't draw anything")
    elif val2 == 1:
        pass
    elif val2 == 2:
        pass
    elif val2 >= 2:
        #algo
        space = ' '
        line = ("|" + (space * (val1 - 2)) + "|")
        print(line)
    else:
        print(" unexpected event ")


def draw_up_line(val1):
    if val1 == 0:
        print(" can't draw anything")
    elif val1 == 1:
        print("o")
    elif val1 == 2:
        print("oo")
    elif val1 >= 2:
        #algo
        spe = '-'
        print("o" + (spe * (val1 - 2)) + "o")
        #...
    else:
        print(" unexpected event ")


try:
    horizon = int(sys.argv[1])
    vertical = int(sys.argv[2])
except:
    sys.exit(" Error ")


draw_geometric(horizon, vertical)