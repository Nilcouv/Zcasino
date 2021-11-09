###### IMPORT #####
import menu.py
from random import randrange

##### SOFTWARE #####
print("Bienvenu dans le jeu Zcasino! \nTentez votre chance au jeu de la roulette pour peut être faire fortune!")
# boucle du programme
replay=True
while replay:
    # initialisation de la partie
    case_min = 1
    case_max = 50    
    solde = 200
    print("Votre solde est actuellement de ", solde, " $.")
    # boucle de partie
    game = True
    while game:
        # Demande au joueur quelle case de la roulette il veut sélectionner
        case = 0
        case = menu.getcase(case_min,case_max)
        # Demande la mise du joueur
        mise = 0
        mise = menu.getmise(solde)
        # Génération de la case aléatoire
        randcase = 0
        randcase = randrange(case_min, case_max)
        # Comparaison de la case aléatoire avec la case sélectionnée par le joueur
        if case == randcase:
            mise *= 3
            print("Bravo! Vouz avez gagnez! \n vous remportez ", mise, " $ !")
            solde += mise
            print("Votre solde est actuellement de ", solde, " $.")
        else:
            print("Désolé! Vous avez perdu.")
            solde -= mise
            print("Votre solde est actuellement de ", solde, " $.")
        # Demande au joueur si il veut continuer à miser
        if solde == 0:
            print("Vous n'avez plus d'argent! Fin de la partie. Bonne journée")
        else:
            game=menu.getcontinue()
    # Demande au joueur si il veut rejouer
    replay = menu.getreplay

#fin du programme
input("Appuyez sur ENTRÉE pour fermer le programme.")
