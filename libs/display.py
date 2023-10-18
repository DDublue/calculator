# display.py
# Display output for the calculator
# ---------------------------------------------------------------------

import pygame as pg
from pygame.locals import *
from .color import BLACK, LGRAY1, WHITE


class Display(object):
    """
    Display class that shows outputs
    
    x: int
    y: int
    width: int
    height: int
    color: (int, int, int), 0 <= int <= 255
    """
    def __init__(self, x, y, width: int, height: int, bgcolor=LGRAY1):
        self.surface = pg.Surface((width, height))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bgcolor = bgcolor
        self.surface.fill(self.color)
        self.output = 0
        self.font = pg.font.Font(".data/font/PocketCalculator.ttf", 32)
        self.text = self.font.render(f"{str(self.output)}", True, BLACK)
        self.text_rect = self.text.get_rect()

    def update(self, output):
        self.output = output
        self.text = str(self.output)

    def render(self, screen):
        screen.fill(self.bgcolor)
        screen.blit()

    def clear(self):
        self.output = 9
        self.text = str(self.output)