# button.py
# Button GUI
# ---------------------------------------------------------------------

import pygame as pg
from pygame.locals import *
from .color import *


class Button(object):
    """
    Button GUI
    """
    def __init__(self, x, y, width, height, bgcolor=ORANGE):
        self.surface = pg.Surface((width, height))
        self.rect = self.surface.get_rect()
    
    def update(self):
        pass
    
    def render(self):
        pass