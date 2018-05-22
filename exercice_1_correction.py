# Proposition de correction
import json

def exercice_1():
    """ Créer un fichier texte (carte.txt) contenant la variable text """
    text = "WWWW-----W\nW-------WW\nWWW-M--WWW\nWWWWWW--WW"
    with open("carte.txt", "w") as my_file:
        my_file.write(text)

def exercice_2():
    """ Afficher en console le fichier texte créé à l'exercice 1 """
    with open("carte.txt", "r") as my_file:
        for line in my_file.readlines():
            print(line.replace("\n", ""))

def exercice_3(lettre):
    """
    Vérifier si la lettre entrée en paramètre est présente
    dans le fichier créé à l'exercice 1 (retourner True si
    la lettre est présente et False sinon)
    """
    is_present = False
    with open("carte.txt", "r") as my_file:
        for line in my_file.readlines():
            if lettre in line:
                is_present = True
    return is_present

def exercice_4(lettre):
    """
    Trouver la position de la lettre passée en paramètre dans
    le fichier créé à l'exercice 1. Si lettre == "M", la fonction
    doit renvoyer le tuple (4, 2) car le lettre "M" est dans la colonne
    4 (numérotation à partir de 0) et la ligne 2 dans la variable text de
    l'exercice 1.
    """
    line_char = 0
    column_char = 0
    with open("carte.txt", "r") as my_file:
        for nb_line, line in enumerate(my_file.readlines()):
            if lettre in line:
                line_char = nb_line
                column_char = line.index(lettre)
    return column_char, line_char

def exercice_5():
    """
    Créer un dictionnaire contenant toutes les lettres présentes
    dans le fichier texte de l'exercice avec leur nombre d'apparition
    dans le fichier : {"W": 22, "M": 1}
    """
    dict_char = {}
    with open("carte.txt", "r") as my_file:
        for line in my_file.readlines():
            for char in line:
                if char in dict_char:
                    dict_char[char] += 1
                else:
                    dict_char[char] = 1
    return dict_char

def exercice_6():
    """ Tranformer le fichier texte de l'exercice 1 en fichier JSON """
    text = {"1":"WWWW-----W", "2":"W-------WW", "3":"WWW-M--WWW", "4":"WWWWWW--WW"}
    with open("carte.json", "w") as my_file:
        my_file.write(json.dumps(text, indent=4))

def exercice_7():
    """
    Demander si le joueur veut continuer le jeu (avec input). Si la
    réponse est "oui", on repose la même question. Si la réponse
    est "non", la boucle s'arrête. Si une autre réponse est donnée,
    afficher "Réponse non correcte" puis reposer la question.
    """
    test = True
    while test:
        answer = input("Voulez-vous continuer à jouer? (oui/non)")
        if answer=="non":
            test=False
        elif answer!="oui":
            print("Réponse non correcte")

if __name__ == "__main__":
    exercice_1()
    print("Réponse de l'exercice 2 :")
    exercice_2()
    print("Réponse de l'exercice 3 :")
    print(exercice_3("-"))
    print("Réponse de l'exercice 4 :")
    print(exercice_4("M"))
    print("Réponse de l'exercice 5 :")
    print(exercice_5())
    exercice_6()
    print("Réponse de l'exercice 7 :")
    exercice_7()
