""" Feu: OK """

# Same one as in the earth challenge

import random

complain1 = " ... les exos du feux me font parler latin à l'envers (un exorciste, vite !) !!! "
complain2 = " ... je prévois tout de même de faire une expédition punitive pour aller taper Harry (snif). "
complain3 = " ... j'ai du sacrifier 30 chattons pour réussir ces p#tains d'épreuves (tout est de ta faute Harry) ! "

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

print(" Après avoir planifié la destruction de la création toute entière ...")
print("... je suis très heureux d'avoir enfin terminer l'épreuve du feu...")
print("... et je compte bien fêter ça comme il se doit ! ! !   :-D ")
print("... même si... %s " % (randomChoice))