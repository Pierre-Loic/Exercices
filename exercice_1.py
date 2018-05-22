

def exercice_1():
    # Créer un fichier texte (carte.txt) contenant la variable text
    text = "WWWW-----W\nW-------WW\nWWW-M--WWW\nWWWWWW--WW"

def exercice_2():
    # Afficher en console le fichier texte créé à l'exercice 1
    pass

def exercice_3(lettre):
    # Vérifier si la lettre entrée en paramètre est présente
    # dans le fichier créé à l'exercice 1 (retourner True si
    # la lettre est présente et False sinon)
    pass

def exercice_4(lettre):
    # Trouver la position de la lettre passée en paramètre dans
    # le fichier créé à l'exercice 1. Si lettre == "M", la fonction
    # doit renvoyer le tuple (4, 2) car le lettre "M" est dans la colonne
    # 4 (numérotation à partir de 0) et la ligne 2 dans la variable text de
    # l'exercice 1.
    pass

def exercice_5():
    # Créer un dictionnaire contenant toutes les lettres présentes
    # dans le fichier texte de l'exercice avec leur nombre d'apparition
    # dans le fichier : {"W": 22, "M": 1}
    pass

def exercice_6():
    # Tranformer le fichier texte de l'exercice 1 en fichier JSON
    pass

def exercice_7():
    # Demander si le joueur veut continuer le jeu (avec input). Si la
    # réponse est "oui" ou "o", on repose la même question. Si la réponse
    # est "non" ou "n", la boucle s'arrête. Si une autre réponse est donnée,
    # afficher "Réponse non correcte" puis reposer la question.
    pass
    
if __name__ == "__main__":    
    exercice_1()
    exercice_2()
    print(exercice_3("M"))
    print(exercice_4("M"))
    exercice_5()
    exercice_6()
    exercice_7()
