# //////////////////////////////////////////////////////////////////
# Effectuer les importations de packages nécessaires pour l'exercice
# //////////////////////////////////////////////////////////////////
import pygame

# /////////////////////////////////////////////////////////
# Ajouter toutes les constantes nécessaires pour l'exercice
# /////////////////////////////////////////////////////////
# ---------
# Constants
# ---------
# -----------
# Window data
# -----------
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
# -----------
# Files paths
# -----------
MACGYVER_PIC = ""
GUARDIAN_PIC = ""
WALL_PIC = ""
PATH_PIC = ""
NEEDLE_PIC = ""
ETHER_PIC = ""
TUBE_PIC = ""


class Game:

    def __init__(self):
        # //////////////////
        # Initialiser Pygame
        # //////////////////
        pass

    def store_map(self):
        # ////////////////////////////////////
        # Stocker le labyrinthe dans une liste
        # ////////////////////////////////////
        pass

    def show_map_console(maze):
        # //////////////////////////////////////
        # Afficher le labyrinthe dans la console
        # //////////////////////////////////////
        pass

    def show_map_pygame(self, maze):
        # //////////////////////////////////
        # Afficher le labyrinthe dans pygame
        # //////////////////////////////////
        pass

    def random_pos(self):
        # ///////////////////////////////////////
        # Positionner MacGyver dans le labyrinthe
        # ///////////////////////////////////////
        pass

class Element:

    def __init__(self, elt):
        # ////////////////////////////////////////////////////////////////////////////////////////////
        # Définir la position initiale et le type d'élèment (éther, aiguille, tube, MacGyver, gardien)
        # ////////////////////////////////////////////////////////////////////////////////////////////
        pass

class Player(Element):

    def __init__(self):
        # //////////////////////////////////////////////////////////////
        # Créer une liste pour stocker les objets collectés par MacGyver
        # //////////////////////////////////////////////////////////////
        pass

    def move(self):
        # /////////////////////////////////////
        # Déplacer le joueur dans le labyrinthe
        # /////////////////////////////////////
        pass


if __name__ == "__main__":
    game = Game()


