""" Feu: OK """

# Same one as in the earth challenge

import random

complain1 = " ... les exos eau00 et eau01 me les ont brisées au dernier degrès !!! "
complain2 = " ... j'envisage d'apprendre la magie noire et les rituels sacrificiels pour réussir la suite des épreuves !"
complain3 = " ...c\'est pas le foutage de g**** qui manque! \n Fonction sort() interdite\n Tu attends l\'exo n°12 du niveau \"EAU\" pour que l\'on te dise \"crée un truc qui remplace sort()\" !!!\n Je vous hais !!! "

randomChoice = random.randint(1, 3)
if randomChoice == 1:
    randomChoice = complain1
    print(complain1)
elif randomChoice == 2:
    randomChoice = complain2
    print(complain2)
elif randomChoice == 3:
    randomChoice = complain3
    print(complain3)
else:
    print(" si cette phrase s'affiche, alors j'ai foiré mon programme  :^) ")

print(" Après avoir hurlé et maudit l'univers au moins 100 fois ...")
print("... je suis plutôt heureux d'avoir terminer l'épreuve de l'eau...")
print("... même si... %s " % (randomChoice))