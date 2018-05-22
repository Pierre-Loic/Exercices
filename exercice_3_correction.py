import pygame
from pygame.locals import *
import time


class Exercices:

    def __init__(self):
        pygame.init()
        self.carte = list(list())
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
                WWWWWWWWWWWWWW
                WW----M------W
                W----WWWWW---W
                WW--WWWWWWWWWW
                WW-----WWWWWWW
                WWW----------W
                WWWW------WWWW
                WWW----W----WW
                WW--WWWWW----W
                WW----WWWWW--W
                WWW----------W
                WWWW--------WW
                WWWWWW----WWWW
                WWWWWWWWWWWWWW
        Ouvrir le fichier carte.txt et ranger les lettres dans une liste à 2 dimensions :
            par exemple, self.carte[1][6] doit être égal à "M"
        Afficher la carte dans la console
        Afficher avec pygame la carte avec les 3 différents sprites (mur, couloir et MacGyver)
        """
        carte = ("WWWWWWWWWWWWWW\n"
                 "WW----M------W\n"
                 "W----WWWWW---W\n"
                 "WW--WWWWWWWW-W\n"
                 "WW-----WWWWWWW\n"
                 "WWW---------WW\n"
                 "WWWW------WWWW\n"
                 "WWW----W----WW\n"
                 "WW--WWWWW----W\n"
                 "WW----WWWWW--W\n"
                 "WWW---------WW\n"
                 "WWWW--------WW\n"
                 "WWWWWW----WWWW\n"
                 "WWWWWWWWWWWWWW")
        # -----------------------------------
        # Write the map in the file carte.txt
        # -----------------------------------
        with open("carte.txt", "w") as file_w:
            file_w.write(carte)
        # -----------------------------------
        # Read the map and put it into a list
        # -----------------------------------
        with open("carte.txt", "r") as file_r:
            for line in file_r:
                self.carte.append([char for char in line if char != "\n"])
        # ------------------------
        # Print the map in console
        # ------------------------
        for i, line in enumerate(self.carte):
            for j, char in enumerate(line):
                print(self.carte[i][j], end="")
            print("")
        # -----------------
        # Print with Pygame
        # -----------------
        for i, line in enumerate(self.carte):
            for j, char in enumerate(line):
                if char == "W":
                    self.fenetre.blit(self.mur, (40 * j, 40 * i))
                if char == "M":
                    self.fenetre.blit(self.macgyver, (40 * j, 40 * i))
                if char == "-":
                    self.fenetre.blit(self.couloir, (40 * j, 40 * i))
        pygame.display.flip()

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
        # ----------------------------------------------------------
        # Find the position of the letter "M" in the list self.carte
        # ----------------------------------------------------------
        m_line = 0
        m_col = 0
        for i, line in enumerate(self.carte):
            for j, char in enumerate(line):
                if char == "M":
                    m_line = i
                    m_col = j
        print(" m_line : " + str(m_line))
        print(" m_col : " + str(m_col))
        # -------------------------
        # Collect inputs from users
        # -------------------------
        test = True
        while test:
            answer = input("Choisissez une lettre pour déplacer le joueur? (N,S,E,W) ou Q pour quitter")
            if answer == "Q":
                test = False
            elif answer == "N":
                if self.carte[m_line - 1][m_col] == "-":
                    self.carte[m_line - 1][m_col] = "M"
                    self.carte[m_line][m_col] = "-"
                    m_line -= 1
                else:
                    print("Le mouvement n'est pas possible car il y a un mur!")
            elif answer == "S":
                if self.carte[m_line + 1][m_col] == "-":
                    self.carte[m_line + 1][m_col] = "M"
                    self.carte[m_line][m_col] = "-"
                    m_line += 1
                else:
                    print("Le mouvement n'est pas possible car il y a un mur!")
            elif answer == "E":
                if self.carte[m_line][m_col + 1] == "-":
                    self.carte[m_line][m_col + 1] = "M"
                    self.carte[m_line][m_col] = "-"
                    m_col += 1
                else:
                    print("Le mouvement n'est pas possible car il y a un mur!")
            elif answer == "W":
                if self.carte[m_line][m_col - 1] == "-":
                    self.carte[m_line][m_col - 1] = "M"
                    self.carte[m_line][m_col] = "-"
                    m_col -= 1
                else:
                    print("Le mouvement n'est pas possible car il y a un mur!")
            else:
                print("Réponse non correcte")
            # ------------------------
            # Print the map in console
            # ------------------------
            for i, line in enumerate(self.carte):
                for j, char in enumerate(line):
                    print(self.carte[i][j], end="")
                print("")


if __name__ == "__main__":
    exercice = Exercices()
