import pygame
from pygame.locals import *

class Exercices:

    def __init__(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((500, 500))
        self.mur = pygame.image.load("mur.png").convert()
        self.macgyver = pygame.image.load("macgyver.png").convert()
        #self.exercice_2("W")
        self.exercice_3()
        self.exercice_1()

    def exercice_1(self):
        """
        Afficher le mot "haut" en console quand on appuie sur la touche fléche vers le haut,
        "bas" quand on appuie sur la touche fléche vers le bas et de même pour les autres
        directions
        """
        boucle = True
        while boucle:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        print("droite")
                    elif event.key == K_LEFT:
                        print("gauche")
                    elif event.key == K_UP:
                        print("haut")
                    elif event.key == K_DOWN:
                        print("bas")
                        boucle = False

    def exercice_2(self, elt):
        """
        Afficher avec pygame le sprite d'un mur si elt="W" et le sprite de MacGyver
        si elt="M"
        """
        if elt=="W":
            self.fenetre.blit(self.mur, (0,0))
        if elt=="M":
            self.fenetre.blit(self.macgyver, (0,0))
        pygame.display.flip()

    def exercice_3(self):
        """
        Afficher avec pygame les sprites suivants "WWWMWMWW"
        """
        map = "WWWMWMWW"
        for i, elt in enumerate(map):
            if elt=="W":
                self.fenetre.blit(self.mur, (40*i,0))
            if elt=="M":
                self.fenetre.blit(self.macgyver, (40*i,0))
        pygame.display.flip()

if __name__=="__main__":
    exercice = Exercices()
