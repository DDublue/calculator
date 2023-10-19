# button.py
# Button GUI
# ---------------------------------------------------------------------

import pygame as pg
from pygame.locals import *
from .color import BLACK, LGRAY1, LGRAY2, DGRAY1


class Button(object):
    """
    Button GUI
    """
    def __init__(self, char, x, y, width=100, height=100, color=LGRAY1):
        self.surf = pg.Surface((width, height))
        self.surf_rect = self.surf.get_rect()
        self._char = char
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = pg.font.Font("./data/font/PocketCalculator.ttf", 32)
        self.text = self.font.render(self._char, True, BLACK)
        self.text_rect = self.text.get_rect()
    
    def update(self): # update when button color is hover, in pressed state, and normal
        pass
    
    def render(self, screen):
        pass

    @property
    def char(self):
        return self._char

    def button_pressed(self):
        if pg.MOUSEBUTTONDOWN:
            if self.surf_rect.collidepoint(pg.mouse.get_pos()):
                return True
        else:
            return False
