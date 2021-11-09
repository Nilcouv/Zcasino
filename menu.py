"""Module reprenant les différents menus à afficher dans Zcasino"""
def getcase(case_min=0,case_max=49):
    """Fonction affichant un menu demandant au joueur quelle case de la roulette il sélectionne,
    prenant en entrée le minimum et le maximum et la roulette et renvoyant en sortie le nombre sélectionné."""
    case = case_min - 1
    while case < case_min or case > case_max:
        print("Quelle case de la roulette voulez-vous sélectionner entre ", case_min, " et ", case_max, "?")
        case = input("Réponse : ")
        try:
            case = int(case)
        except ValueError:
            print("Veuillez entrer un nombre")
            case = case_min - 1
            continue
        if case >= case_min and case <= case_max:
            print("Vous avez sélectionné la case n°", case)
            replayMenu = False
        else:
            print("Veuillez sélectionner une case comprise entre ",case_min," et ", case_max," !")
    # Sortie du menu et renvoie la mise du joueur
    return case
    
def getmise(solde=0):
    """Fonction affichant un menu demandant à l'utilisateur d'entrer le montant qu'il veut miser,
    qui accepte en entré le solde de l'utilisateur et qui renvoie en sortie un nombre"""
    mise = 0
    while mise <= 0 or mise>solde:        
        mise = input("Quelle montant en Dollars voulez-vous miser? \nRéponse : ")
        try:
            mise = int(mise)
        except ValueError:
            print("Veuillez entrer un nombre")
            mise = 0
            continue
        if mise > solde:
            print("Solde insuffisant!")
        elif mise <= 0:
            print("La mise ne peut être inférieur ou égale à 0")            
        else:
            print("Vous misez : ", mise,"$")
    # Sortie du menu et renvoie la mise du joueur
    return mise

def getcontinue():
    """Fonction demandant à l'utilisateur si il veut continuer à miser, et retournant "True" ou "False" en fonction de sa réponse"""
    replayMenu=True
    while replayMenu:
        answer = input("Voulez-vous de nouveau miser? (O/N) \nRéponse : ")

        if answer == "O" or answer == "o" or answer == "Oui" or answer == "oui":
            replayMenu = False
            return True
        elif answer == "N" or answer == "n" or answer == "Non" or answer == "non":
            replayMenu = False
            return False
        else:
            print("Veuillez entrer une réponse valide!")
            
def getreplay():
    """Fonction demandant à l'utilisateur si il veut continuer à jouer, et retournant "True" ou "False" en fonction de sa réponse"""
    replayMenu=True
    while replayMenu:
        answer = input("Voulez-vous rejouer une partie? (O/N) \nRéponse : ")

        if answer == "O" or answer == "o" or answer == "Oui" or answer == "oui":
            replayMenu = False
            return True
        elif answer == "N" or answer == "n" or answer == "Non" or answer == "non":
            replayMenu = False
            return False
        else:
            print("Veuillez entrer une réponse valide!")
