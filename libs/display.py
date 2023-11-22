# display.py
# Display output for the calculator
# ---------------------------------------------------------------------

import pygame as pg
from pygame.locals import *
from .color import BLACK, LGRAY1, LGRAY2, WHITE


class Display(object):
    """
    Display class that shows outputs
    
    x: int
    y: int
    width: int
    height: int
    color: (int, int, int), 0 <= int <= 255
    """
    def __init__(self, x, y, width: int, height: int, bgcolor=LGRAY2):
        self.surf = pg.Surface((width, height))
        self.surf_rect = self.surf.get_rect(centerx=x)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        self.output = "0"
        self.font = pg.font.Font("./data/font/PocketCalculator.ttf", 70)
        self.text = self.font.render(f"{str(self.output)}", True, BLACK)
        self.text_rect = self.text.get_rect(bottomright=(self.width, self.height))

    def update(self, output):
        self.text = self.font.render(f"{output}", True, BLACK)
        self.text_rect = self.text.get_rect(bottomright=(self.width-10, self.height+8))

    def render(self, screen):
        screen.blit(self.surf, self.surf_rect)
        self.surf.fill(self.bgcolor)
        self.surf.blit(self.text, self.text_rect)

    def clear(self):
        self.output = 0
        self.text = self.font.render(f"{str(self.output)}", True, BLACK)
        self.text_rect = self.text.get_rect()