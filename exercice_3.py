import pygame
from pygame.locals import *

class Exercices:

    def __init__(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((560, 560))
        self.mur = pygame.image.load("mur.png").convert()
        self.couloir = pygame.image.load("couloir.png").convert()
        self.macgyver = pygame.image.load("macgyver.png").convert()
        self.exercice_1()
        self.exercice_2()
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0

    def exercice_1(self):
        """
        Créer un fichier carte.txt avec les élèments "W", "-" et "M" :
                WWWWWWWWWWWWWWW
                WW----M-------W
                W----WWWWW----W
                WW--WWWWWWWWW-W
                WW-----WWWWWWWW
                WWW----------WW
                WWWW------WWWWW
                WWW----W----WWW
                WW--WWWWW----WW
                WW----WWWWW---W
                WWW----------WW
                WWWW--------WWW
                WWWWWW----WWWWW
                WWWWWWWWWWWWWWW
        Ouvrir le fichier carte.txt et ranger les lettres dans une liste à 2 dimensions :
            par exemple, self.carte[1][6] doit être égal à "M"
        Afficher la carte dans la console
        Afficher avec pygame la carte avec les 3 différents sprites (mur, couloir et MacGyver)
        """
        pass

    def exercice_2(self):
        """
        Demander au joueur de rentrer une lettre : "N", "S", "W" et "E"
        S'il rentre une lettre différente, il faut lui reposer la question
        S'il rentre "N", la lettre "M" se déplace vers la haut dans la liste à 2 dimensions de l'exercice 1 self.carte
        S'il rentre "S", la lettre "M" se déplace vers la bas dans la liste à 2 dimensions de l'exercice 1 self.carte
        S'il rentre "E", la lettre "M" se déplace vers la droite dans la liste à 2 dimensions de l'exercice 1 self.carte
        S'il rentre "W", la lettre "M" se déplace vers la gauche dans la liste à 2 dimensions de l'exercice 1 self.carte
        Puis on repose la question pour un autre mouvement...
        """
        pass

if __name__=="__main__":
    exercice = Exercices()
