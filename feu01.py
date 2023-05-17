""" Evaluer une expression """

# Créer un programme qui reçoit une expression arithmétique dans une chaîne de caractères et en retourne le résultat après l'avoir calculé.

# Il est impératif de gérer les 5 opérateurs suivants: "+" addition   "-" soustraction   "*" multiplication   "/" division   "%" modulo

# feu01.py " 4 + 21 * ( 1 - 2 / 2) + 38"            resultat = 42

""" parser, lexer, ast, arbre binaire, recursive descent parser """
import sys

fuckingMath = 2 + 4 * 8 - 1
print(fuckingMath)

fuckingMath2 = "2 + 4 * 8 - 1"
print(fuckingMath2)

fuckingMath3 = 4 + 21 * (1 - 2 / 2) + 38
print(fuckingMath3)

#fucking_Math = 4 + 21 * (1 - 2 / 2) + 38
#fucking_Math = 4 + 21 * (1 - 1) + 38
#fucking_Math = 4 + 21 * 0 + 38
#fucking_Math = 4 + 0 + 38
#fucking_Math = 42

crazy_math = "4 + 21 * ( 1 - 2 / 2 ) + 38"

silly_math = "4 + 2 * 2"

# Cut the string and display each elements over one another
def split_func(arg):
    list_math = arg.split(" ")
    print(list_math)
    print(*crazy_math, sep='\n')
    #return list_math
    do_multiply(list_math)

def do_multiply(isList):
    for val in isList :
        if val == "*":
            print(isList[-1])

# arg input
"""try:
    myInput = sys.argv[1] # "Hello my dudes  :-D"
except IndexError:
    sys.exit(" ERROR ")"""

split_func(silly_math)
do_multiply()