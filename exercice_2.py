import pygame
from pygame.locals import *

class Exercices:

    def __init__(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((500, 500))
        self.mur = pygame.image.load("mur.png").convert()
        self.macgyver = pygame.image.load("macgyver.png").convert()
        self.exercice_2("W")
        #self.exercice_3()
        self.exercice_1()

    def exercice_1(self):
        """
        Afficher le mot "haut" en console quand on appuie sur la touche fléche vers le haut,
        "bas" quand on appuie sur la touche fléche vers le bas et de même pour les autres
        directions
        """
        pass

    def exercice_2(self, elt):
        """
        Afficher avec pygame le sprite d'un mur si elt="W" et le sprite de MacGyver
        si elt="M"
        """
        pass

    def exercice_3(self):
        """
        Afficher avec pygame les sprites suivants "WWWMWMWW"
        """
        pass

if __name__=="__main__":
    exercice = Exercices()
