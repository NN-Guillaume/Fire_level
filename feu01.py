""" Evaluer une expression """

# Créer un programme qui reçoit une expression arithmétique dans une chaîne de caractères et en retourne le résultat après l'avoir calculé.

# Il est impératif de gérer les 5 opérateurs suivants: "+" addition   "-" soustraction   "*" multiplication   "/" division   "%" modulo

# feu01.py " 4 + 21 * ( 1 - 2 / 2) + 38"            resultat = 42

""" parser, lexer, ast, arbre binaire, recursive descent parser """

def math_interpreter(expression):
    # Remove whitespaces from the expression
    expression = expression.replace(" ", "")

    # Check for balanced parentheses
    if not check_balanced_parentheses(expression):
        return "Error: Unbalanced parentheses"

    try:
        result = eval(expression)
        return result
    except (SyntaxError, NameError, TypeError) as e:
        return "Error: Invalid expression"

def check_balanced_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Example usage:
expression = input("Enter a mathematical expression: ")
result = math_interpreter(expression)
print("Result:", result)
