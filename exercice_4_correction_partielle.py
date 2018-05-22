# //////////////////////////////////////////////////////////////////
# Effectuer les importations de packages nécessaires pour l'exercice
# //////////////////////////////////////////////////////////////////
import pygame
import random
from pygame.locals import *
from ex4_constants import *

class Game:

    def __init__(self):
        # //////////////////
        # Initialiser Pygame
        # //////////////////
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.maze = list(list())
        # Creation of all the elements
        self.macgyver = Player()
        self.wall = Element("wall")
        self.path = Element("path")
        self.store_map()
        self.show_map_console()
        self.show_map_pygame(self.maze)
        self.random_pos(self.maze, self.macgyver)
        self.show_map_console()
        self.macgyver.move("W")
        self.show_map_console()
        self.continuer = True
        while self.continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.continuer = 0

    def store_map(self):
        # ////////////////////////////////////
        # Stocker le labyrinthe dans une liste
        # ////////////////////////////////////
        with open("carte.txt", "r") as file_r:
            for line in file_r:
                self.maze.append([char for char in line if char != "\n"])

    def show_map_console(self):
        # //////////////////////////////////////
        # Afficher le labyrinthe dans la console
        # //////////////////////////////////////
        for i, line in enumerate(self.maze):
            for j, char in enumerate(line):
                print(self.maze[i][j], end="")
            print("")

    def show_map_pygame(self, maze):
        # //////////////////////////////////
        # Afficher le labyrinthe dans pygame
        # //////////////////////////////////
        for i, line in enumerate(maze):
            for j, char in enumerate(line):
                if char == self.wall.letter:
                    self.window.blit(self.wall.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.macgyver.letter:
                    self.window.blit(self.macgyver.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.path.letter:
                    self.window.blit(self.path.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
        pygame.display.flip()

    @staticmethod
    def find_pos(maze, elt):
        """ Find the position of a letter in the maze """
        m_line = 0
        m_col = 0
        for i, line in enumerate(maze):
            for j, char in enumerate(line):
                if char == elt.letter:
                    m_line = i
                    m_col = j
        return m_line, m_col

    def random_pos(self, maze, elt):
        # ///////////////////////////////////////
        # Positionner MacGyver dans le labyrinthe
        # ///////////////////////////////////////
        pass

class Element:

    def __init__(self, elt):
        # ////////////////////////////////////////////////////////////////////////////////////////////
        # Définir la position initiale et le type d'élèment (éther, aiguille, tube, MacGyver, gardien)
        # ////////////////////////////////////////////////////////////////////////////////////////////
        if elt=="macgyver":
            self.image = pygame.image.load(MACGYVER_PIC).convert()
            self.letter = "M"
        elif elt=="wall":
            self.image = pygame.image.load(WALL_PIC).convert()
            self.letter = "W"
        elif elt=="path":
            self.image = pygame.image.load(PATH_PIC).convert()
            self.letter = "-"
        self._x = 0
        self._y = 0

    def pos_x(self, x=None):
        if x:
            self._x = x
        return self._x

    def pos_y(self, y=None):
        if y:
            self._y = y
        return self._y

class Player(Element):

    def __init__(self):
        # //////////////////////////////////////////////////////////////
        # Créer une liste pour stocker les objets collectés par MacGyver
        # //////////////////////////////////////////////////////////////
        Element.__init__(self, "macgyver")
        self.list_obj = []

    def move(self, dir):
        # /////////////////////////////////////
        # Déplacer le joueur dans le labyrinthe
        # /////////////////////////////////////
        if dir=="N":
            self.pos_y(self.pos_y()-1)
        elif dir=="S":
            self.pos_y(self.pos_y()+1)
        elif dir=="E":
            self.pos_x(self.pos_x()+1)
        elif dir=="W":
            self.pos_x(self.pos_x()-1)

if __name__ == "__main__":
    game = Game()


