
from time import sleep
import random
import pygame

LEN_SNAKE = 13


class Fruit:
    def __init__(self, color, position_x, position_y):
        self.color = color
        self._position_x = position_x
        self._position_y = position_y
        self.width = LEN_SNAKE
        self.height = LEN_SNAKE
        self.fruit_rect = 0

    def draw_fruit(self, screen):
        self.fruit_rect = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height)
        pygame.draw.rect(screen, self.color, [
                         self.position_x, self.position_y, self.width, self.height])

    def change_position(self, size_screen):
        self.position_x = random.randint(1, size_screen[0]-LEN_SNAKE)
        self.position_y = random.randint(1, size_screen[1]-LEN_SNAKE)

    # ----------- Getters e Setters -----------------

    @property
    def position_x(self):
        return self._position_x

    @position_x.setter
    def position_x(self, valor):
        self._position_x = valor

    @property
    def position_y(self):
        return self._position_y

    @position_y.setter
    def position_y(self, valor):
        self._position_y = valor

    def get_position(self):
        return self.position_x, self.position_y
