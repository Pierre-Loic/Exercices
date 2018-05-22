# //////////////////////////////////////////////////////////////////
# Effectuer les importations de packages nécessaires pour l'exercice
# //////////////////////////////////////////////////////////////////
import pygame
import random
from pygame.locals import *
import time
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
        self.macgyver.y = self.find_pos(self.macgyver)[0]
        self.macgyver.x = self.find_pos(self.macgyver)[1]
        self.show_map_pygame()
        time.sleep(2)
        # Random position for MacGyver
        self.random_pos(self.macgyver)
        self.show_map_pygame()
        time.sleep(2)
        # Move MacGyver
        time.sleep(2)
        self.update_pos("W")
        self.show_map_pygame()
        # -------------------
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

    def show_map_pygame(self):
        # //////////////////////////////////
        # Afficher le labyrinthe dans pygame
        # //////////////////////////////////
        for i, line in enumerate(self.maze):
            for j, char in enumerate(line):
                if char == self.wall.letter:
                    self.window.blit(self.wall.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.macgyver.letter:
                    self.window.blit(self.macgyver.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.path.letter:
                    self.window.blit(self.path.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
        pygame.display.flip()

    def find_pos(self, elt):
        """ Find the position of a letter in the maze """
        m_line = 0
        m_col = 0
        for i, line in enumerate(self.maze):
            for j, char in enumerate(line):
                if char == elt.letter:
                    m_line = i
                    m_col = j
        return m_line, m_col

    def random_pos(self, elt):
        # ///////////////////////////////////////
        # Positionner MacGyver dans le labyrinthe
        # ///////////////////////////////////////
        line, col = self.find_pos(elt)
        char=""
        rand_line = 0
        rand_char = 0
        # Check if it is a wall or not
        while char!="-":
            rand_line = random.randint(0, len(self.maze)-1)
            rand_char = random.randint(0, len(self.maze[0])-1)
            char = self.maze[rand_line][rand_char]
        self.maze[line][col] = "-"
        self.maze[rand_line][rand_char] = elt.letter
        elt.x = rand_char
        elt.y = rand_line

    def update_pos(self, direction):
        self.maze[self.macgyver.y][self.macgyver.x] = "-"
        self.macgyver.move(direction)
        self.maze[self.macgyver.y][self.macgyver.x] = "M"

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

    def _get_x(self):
        return self._x

    def _set_x(self, new_x):
        self._x = new_x

    def _get_y(self):
        return self._y

    def _set_y(self, new_y):
        self._y = new_y

    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)

class Player(Element):

    def __init__(self):
        # //////////////////////////////////////////////////////////////
        # Créer une liste pour stocker les objets collectés par MacGyver
        # //////////////////////////////////////////////////////////////
        Element.__init__(self, "macgyver")
        self.list_obj = []

    def move(self, direction):
        # /////////////////////////////////////
        # Déplacer le joueur dans le labyrinthe
        # /////////////////////////////////////
        if direction=="N":
            self.y = self.y - 1
        elif direction=="S":
            self.y = self.y + 1
        elif direction=="E":
            self.x = self.x + 1
        elif direction=="W":
            self.x = self.x - 1

if __name__ == "__main__":
    game = Game()


